#!/usr/bin/python
import fitbit
import webbrowser
import datetime
from pymongo import MongoClient
from Crypto.Cipher import AES
from fitbit import Global

class AuthenticateAndFetchFitbitData():
    def __init__(self):
        self.f = fitbit.FitBit()
        self.data = {}
        for user in Global.USERS.split(','):
            self.data[user] = {}

        self.DATE = []
        for i in range(int(Global.DAYS)):
            date = datetime.datetime.now()     - datetime.timedelta(days= (i+1))
            self.DATE += [date.strftime("%Y-%m-%d")]  #The date in the format yyyy-MM-dd or today

    def MakeApiCall(self,token, apistring, user):
        response = self.f.ApiCall(token, apistring)
        return response


    def encrypt(self, plain_text):
        encryption_suite = AES.new('Key ResearchTAMU', AES.MODE_CFB, 'This is an IV456')  #16 bit key
        cipher_text = encryption_suite.encrypt(plain_text)
        return cipher_text.encode('base64','strict')

    def decrypt(self, cipher_text):
        decryption_suite = AES.new('Key ResearchTAMU', AES.MODE_CFB, 'This is an IV456')    #16 bit key
        plain_text = decryption_suite.decrypt(cipher_text.decode('base64','strict'))
        return plain_text

    def Reauthenticate(self, bad_token, name):
        """Called if the currently stored token is not accepted for a user OR if token is missing. Receives the old token which may be null and the user name. Returns new valid token."""
        print
        print "Stored access token %s not accepted for user %s. Reauthenticating. \n" % (bad_token, name)
        auth_url, auth_token = self.f.GetRequestToken()
        webbrowser.open(auth_url)
        PIN = raw_input(" Please paste the PIN that is returned from Fitbit [ENTER]: ")
        #if the PIN is not 26 characters, prompt user - in testing all PINs have been 25 or 26 characters
        if len(PIN) < 25:
            PIN = raw_input("\n Please confirm that you have entered the correct PIN returned from the Fitbit website and repaste here.[ENTER]: ")
        try:
            access_token_new = self.f.GetAccessToken(PIN, auth_token) #This traps error if PIN isn't pasted correctly. In testing some users typed a number & hit ENTER and bad PIN caused error.
        except ValueError:
            self.Reauthenticate(bad_token, name) #If bad PIN try again
        return access_token_new

    def getTokensFromDB(self, users):
        result = {}
        mongoDbClient = MongoClient()
        objDatabaseInstance = mongoDbClient.DevicesData
        for user in users:
            objFitbitAuthenticationCollection = objDatabaseInstance.FitbitAuthenticationData.find({"user_id" :  user})
            if objFitbitAuthenticationCollection.count() == 0 :
                result[user] = ""
            else:
                for document in objFitbitAuthenticationCollection:
                    result[user] = self.decrypt(document["token"])
        return result

    def setTokensToDB(self, user, token):
        mongoDbClient = MongoClient()
        objDatabaseInstance = mongoDbClient.DevicesData
        objFitbitAuthenticationCollection = objDatabaseInstance.FitbitAuthenticationData.find({"user_id" : user})
        if objFitbitAuthenticationCollection.count() == 0 :
            objDatabaseInstance.FitbitAuthenticationData.insert_one({"user_id" : user, "token" : self.encrypt(token)})
        else:
            objDatabaseInstance.FitbitAuthenticationData.update({"user_id" : user}, {"token" : self.encrypt(token) })

    def getData(self,objUsersname):


        access_tokens = self.getTokensFromDB(objUsersname)

        for user in objUsersname:
            for date in self.DATE:
                objAPIString = '/1/user/-/activities/date/' + date + '.json'
                objAPIStringForFood = '/1/user/-/foods/log/caloriesIn/date/' + date + '/1d.json'
                objAPIStringForWater = '/1/user/-/foods/log/water/date/' + date + '/1d.json'
                try:
                    response = self.MakeApiCall(access_tokens[user], objAPIString,user)
                    response += "," + self.MakeApiCall(access_tokens[user], objAPIStringForFood,user)
                    response += "," + self.MakeApiCall(access_tokens[user], objAPIStringForWater,user)
                except ValueError:
                    new_token = self.Reauthenticate(access_tokens[user], user)
                    print "For user %s new access token = %s." % (user, new_token)
                    response = self.MakeApiCall(new_token, objAPIString, user)
                    response += "," + self.MakeApiCall(new_token, objAPIStringForFood,user)
                    response += "," + self.MakeApiCall(new_token, objAPIStringForWater,user)
                    access_tokens[user] = new_token
                    self.setTokensToDB(user, new_token)

                temp = {"date" : date, "todaysummary": response}
                print "Collected data for user: %s for date: %s"%(user,date)
                self.data[user][date] = temp
        return self.data

