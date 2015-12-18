#!/usr/bin/python
from pymongo import MongoClient
import authenticate_and_fetch_fitbit_data
import time

if __name__ == "__main__":

    #Setting up MongDB connection and database: DevicesData & collection: FitbitData
    mongoDbClient = MongoClient()
    db = "DevicesData"
    objDatabaseInstance = mongoDbClient.get_database(db)
    objFitbitCollection = objDatabaseInstance.FitbitData.find()

    #Getting data from fitbit
    users = ["diabetesresearchtamu@gmail.com", "vivektyagi.nith@gmail.com", "aadiuppal@tamu.edu"]
    objFitbitAPIInstance = authenticate_and_fetch_fitbit_data.AuthenticateAndFetchFitbitData()
    dataFromFitbit = objFitbitAPIInstance.getData(users)


    for user in users:
        objFitbitUserDocument = objDatabaseInstance.FitbitData.find({"user_id" : user})    #Document is MongoDB terminology

        if objFitbitUserDocument.count() > 0:                     #Need to update data
            if objDatabaseInstance.FitbitData.find({"data.date": objFitbitAPIInstance.DATE, "user_id" : user}).count() == 0:
                objDatabaseInstance.FitbitData.update({"user_id" : user}, {"$push" : { "data": dataFromFitbit[user]}})
            #Data already there, todo: updated data should be pushed
        else:                                               #fresh insertion
            objDatabaseInstance.FitbitData.insert_one({"user_id": user, "data" : [dataFromFitbit[user]]})
