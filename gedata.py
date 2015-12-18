#!/usr/bin/python
from pymongo import MongoClient



mongoDbClient = MongoClient()
objDatabaseInstance = mongoDbClient.DevicesData

#objFitbitCollection = objDatabaseInstance.FitbitAuthenticationData.insert_one({"user_id" : "diabetesresearchtamu@gmail.com", "token": "oauth_token=d2e270097f9ac1d501df57cd760b2a76&oauth_token_secret=ee0f7ec3c95246c7055654f6c32f1701"})
#objDatabaseInstance.FitbitAuthenticationData.delete_one({"user_id" : "vivektyagi.nith@gmail.com"})

# if True:
if False:
    objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : "diabetesresearchtamu@gmail.com"})
    objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : "vivektyagi.nith@gmail.com"})
    objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : " aadiuppal@tamu.edu"})
    # objFitbitCollection = objDatabaseInstance.FitbitAuthenticationData.delete_one({"user_id" : "diabetesresearchtamu@gmail.com"})
    objFitbitCollection = objDatabaseInstance.FitbitAuthenticationData.delete_one({"user_id" : "vivektyagi.nith@gmail.com"})
    objFitbitCollection = objDatabaseInstance.FitbitAuthenticationData.delete_one({"user_id" : " aadiuppal@tamu.edu"})
else:
    objFitbitCollection = objDatabaseInstance.FitbitData.find()

    print "Fitbit DATA: "
    print
    print objFitbitCollection.count()
    for document in objFitbitCollection:
        print document
        print

    print "________________________________"

    objFitbitAuthCollection = objDatabaseInstance.FitbitAuthenticationData.find()

    print "Fitbit Authentication DATA: "
    print
    print objFitbitAuthCollection.count()
    for document in objFitbitAuthCollection:
        print document
        print