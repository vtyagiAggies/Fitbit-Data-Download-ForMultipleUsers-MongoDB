#!/usr/bin/python
import fitbit
import webbrowser
import os
import csv
import time


class AuthenticateAndFetchFitbitData():
    def __init__(self):
        self.f = fitbit.FitBit()
        self.data = {}
        self.DATE = 'today'

    def MakeApiCall(self,token, apistring, user):
        response = self.f.ApiCall(token, apistring)
        date = time.strftime("%d/%m/%Y")
        temp = {"date" : date, "data": response}
        self.data[user] = temp

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

    def getData(self,objUsername):
        mainfile= '%s.csv' % self.f.TOKENFILENAME #Read from .ini file by fitbit module
        tmpfile= '%s.tmp.csv' % self.f.TOKENFILENAME
        read_token=open(mainfile,'rU')
        csvreader = csv.reader(read_token, dialect='excel', quotechar="'", delimiter=',')
        try:
            accesstokensfile = {rows[0]:rows[1] for rows in csvreader}
        except IndexError:
            ## Need to file read position or else we miss the first input
            read_token.seek(0)
            accesstokensfile = {rows[0]:rows[0] for rows in csvreader}
            ## Assign blank values to all missing keys
            for key in accesstokensfile.keys():
                accesstokensfile[key] = ''
        NamesList = accesstokensfile.keys()
        access_token = accesstokensfile.values()
        ## Remove temporary csv file if it exists
        try:
            os.remove(tmpfile)
        except OSError:
            ## Do nothing - if the tmp file doesn't exist we are happy
            pass

        APISTRING = '/1/user/-/activities/date/' + self.DATE + '.json'


        n=0
        # NamesList = objUsername
        write_token = open(tmpfile, 'wb')
        csvwriter = csv.writer(write_token)
        for value in NamesList:
            try:
                self.MakeApiCall(access_token[n], APISTRING,value)
                csvwriter.writerow([value, access_token[n]])
            except ValueError:
                new_token = self.Reauthenticate(access_token[n], value)
                print "For user %s new access token = %s." % (value, new_token)
                self.MakeApiCall(new_token, APISTRING, value)
                csvwriter.writerow([value, new_token])
            n=n+1

        write_token.flush()
        write_token.close()
        read_token.close()

        i=0
        mainfile_new = mainfile
        while True :
            try:
                if mainfile == mainfile_new:
                    os.remove(mainfile_new)
                os.rename(tmpfile,mainfile_new)
                if mainfile != mainfile_new:
                    print "New file '" + mainfile_new + "' has been created!"
                break
            except OSError:
                if mainfile_new == mainfile:
                    print "Unable to access file '" + mainfile_new + "', please make sure that this file is NOT open on your computer"
                    choice = raw_input("Press 1 to retry access to '" + mainfile_new + "', or press any other key to write to a new file: ")
                    if choice in ('1',''):
                        continue
                mainfile_new = str(i) + '.' + mainfile
                i += 1
        return self.data
