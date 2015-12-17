#!/usr/bin/python
import fitbit
import webbrowser
import datetime
from pymongo import MongoClient
from Crypto.Cipher import AES

class AuthenticateAndFetchFitbitData():
    def __init__(self):
        self.f = fitbit.FitBit()
        self.data = {}
        yesterday = datetime.datetime.now()     - datetime.timedelta(days=1)
        self.DATE = yesterday.strftime("%Y-%m-%d")  #The date in the format yyyy-MM-dd or today

    def MakeApiCall(self,token, apistring, user):
        response = self.f.ApiCall(token, apistring)             #Caluclating for yesterday
        temp = {"date" : self.DATE, "todaysummary": response}
        self.data[user] = temp


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
        print "Stored access token %s not accepted for user %s. Reauthenticating. \n" % (bad_token, name)
        auth_url, auth_token = self.f.GetRequestToken()
        webbrowser.open(auth_url)
        PIN = raw_input("\n Please paste the PIN that is returned from Fitbit [ENTER]: ")
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

        APISTRING = '/1/user/-/activities/date/' + self.DATE + '.json'
        access_tokens = self.getTokensFromDB(objUsersname)

        for value in objUsersname:
            try:
                self.MakeApiCall(access_tokens[value], APISTRING,value)
            except ValueError:
                new_token = self.Reauthenticate(access_tokens[value], value)
                print "For user %s new access token = %s." % (value, new_token)
                self.MakeApiCall(new_token, APISTRING, value)
                self.setTokensToDB(value, new_token)
        return self.data

