"""
A Python library for accessing the FitBit API.

This library provides a wrapper to the FitBit API and does not provide storage of tokens or caching if that is required.

Most of the code has been adapted from: https://groups.google.com/group/fitbit-api/browse_thread/thread/0a45d0ebed3ebccb
"""
import httplib, time, ConfigParser, sys
import oauth2 as oauth

class FitBit():
    #Read global values from config file
    config = ConfigParser.RawConfigParser()
    try:
        cf=open('fitbit_config.ini')
    except IOError:
        sys.exit("Missing or corrupt fitbit_config.ini file in program path! Terminating execution.")
    config.readfp(cf)
    cf.close()
    APP_NAME = config.get('Globals', 'AppName')
    CONSUMER_KEY = config.get('Globals', 'ConsumerKey') 
    CONSUMER_SECRET = config.get('Globals', 'ConsumerSecret') 
    SERVER = config.get('Globals', 'Server')
    REQUEST_TOKEN_URL = 'http://%s/oauth/request_token' % SERVER 
    ACCESS_TOKEN_URL = 'http://%s/oauth/access_token' % SERVER 
    AUTHORIZATION_URL = 'http://%s/oauth/authorize' % SERVER
    TOKENFILENAME = config.get('FileData', 'OutputFilePrefix')
    
    def FetchResponse(self, oauth_request, connection, url): #added URL as config. parameter
        connection.request(oauth_request.method, url, headers=oauth_request.to_header()) #added headers to pass parameters
        response = connection.getresponse()
        s=response.read()
        return s
            
    def GetRequestToken(self): 
        connection = httplib.HTTPSConnection(self.SERVER)
        consumer = oauth.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        signature_method = oauth.SignatureMethod_PLAINTEXT()
        oauth_request = oauth.Request.from_consumer_and_token(consumer, http_url=self.REQUEST_TOKEN_URL)
        oauth_request.sign_request(signature_method, consumer, None)
        resp = self.FetchResponse(oauth_request, connection, self.REQUEST_TOKEN_URL) #passing in explicit url
        auth_token = oauth.Token.from_string(resp) 
        auth_url = "%s?oauth_token=%s" % (self.AUTHORIZATION_URL, auth_token.key) #build the URL
        return auth_url, auth_token
   
    def GetAccessToken(self, access_code, auth_token):
        oauth_verifier = access_code
        connection = httplib.HTTPSConnection(self.SERVER) 
        consumer = oauth.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET) 
        signature_method = oauth.SignatureMethod_PLAINTEXT()
        oauth_request = oauth.Request.from_consumer_and_token(consumer, token=auth_token, http_url=self.ACCESS_TOKEN_URL, parameters={'oauth_verifier': oauth_verifier})
        oauth_request.sign_request(signature_method, consumer, auth_token)
        # now the token we get back is an access token
        access_token = oauth.Token.from_string(self.FetchResponse(oauth_request,connection, self.ACCESS_TOKEN_URL)) # parse the response into an OAuthToken object / passingin explicit url
        # store the access token when returning it
        access_token = access_token.to_string()
        return access_token
   
    def ApiCall(self, access_token, apiCall): #removed original hardcoded api call in favor of string passed from PickApiCall()
        signature_method = oauth.SignatureMethod_PLAINTEXT()
        connection = httplib.HTTPSConnection(self.SERVER) 
        #build the access token from a string
        access_token = oauth.Token.from_string(access_token)
        consumer = oauth.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        final_url = 'http://' + self.SERVER + apiCall
        oauth_request = oauth.Request.from_consumer_and_token(consumer, token=access_token, http_url=final_url)
        oauth_request.sign_request(signature_method, consumer, access_token)
        headers = oauth_request.to_header(realm='api.fitbit.com') 
        connection.request('GET', apiCall, headers=headers) 
        resp = connection.getresponse() 
        response = resp.read() 
        return response
