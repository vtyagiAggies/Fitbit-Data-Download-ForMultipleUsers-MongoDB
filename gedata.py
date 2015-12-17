from pymongo import MongoClient



mongoDbClient = MongoClient()
objDatabaseInstance = mongoDbClient.DevicesData

#objFitbitCollection = objDatabaseInstance.FitbitAuthenticationData.insert_one({"user_id" : "diabetesresearchtamu@gmail.com", "token": "oauth_token=d2e270097f9ac1d501df57cd760b2a76&oauth_token_secret=ee0f7ec3c95246c7055654f6c32f1701"})
#objDatabaseInstance.FitbitAuthenticationData.delete_one({"user_id" : "vivektyagi.nith@gmail.com"})

if False:
    objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : "diabetesresearchtamu@gmail.com"})
    objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : "vivektyagi.nith@gmail.com"})
else:
    objFitbitCollection = objDatabaseInstance.FitbitData.find()
    print objFitbitCollection.count()
    for document in objFitbitCollection:
        print document
        print