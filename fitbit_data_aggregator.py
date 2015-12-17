#!/usr/bin/python
from pymongo import MongoClient
import authenticate_and_fetch_fitbit_data
import time

if __name__ == "__main__":
    #Setting up MongDB connection and database: DevicesData & collection: FitbitData
    mongoDbClient = MongoClient()
    objDatabaseInstance = mongoDbClient.DevicesData
    objFitbitCollection = objDatabaseInstance.FitbitData.find()
    # objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : "diabetesresearchtamu@gmail.com"})
    # objFitbitCollection = objDatabaseInstance.FitbitData.delete_one({"user_id" : "vivektyagi.nith@gmail.com"})

    #Getting data from fitbit
    users = ["diabetesresearchtamu@gmail.com", "vivektyagi.nith@gmail.com"]
    objFitbitAPIInstance = authenticate_and_fetch_fitbit_data.AuthenticateAndFetchFitbitData()
    dataFromFitbit = objFitbitAPIInstance.getData(users)


    for user in users:
        objFitbitUserDocument = objDatabaseInstance.FitbitData.find({"user_id" : user})    #Document is MongoDB terminology


        if objFitbitUserDocument.count() > 0:                     #Need to update data
            if objDatabaseInstance.FitbitData.find({"data.date": objFitbitAPIInstance.DATE}).count() == 0:
                objDatabaseInstance.FitbitData.update({"user_id" : user}, {"$push" : { "data": dataFromFitbit[user]}})
            #Data already there, todo: updated data should be pushed
        else:                                               #fresh insertion
            objDatabaseInstance.FitbitData.insert_one({"user_id": user, "data" : [dataFromFitbit[user]]})

    objFitbitCollection = objDatabaseInstance.FitbitData.find()
    for d in objFitbitCollection:
        print d
        print
        print