#!/usr/bin/python
from pymongo import MongoClient
import authenticate_and_fetch_fitbit_data
from fitbit import Global

if __name__ == "__main__":

    #Setting up MongDB connection and database: DevicesData & collection: FitbitData
    mongoDbClient = MongoClient()
    db = "DevicesData"
    objDatabaseInstance = mongoDbClient.get_database(db)
    objFitbitCollection = objDatabaseInstance.FitbitData.find()

    #Getting data from fitbit
    users = Global.USERS.split(',')
    objFitbitAPIInstance = authenticate_and_fetch_fitbit_data.AuthenticateAndFetchFitbitData()
    dataFromFitbit = objFitbitAPIInstance.getData(users)


    for user in users:
        objFitbitUserDocument = objDatabaseInstance.FitbitData.find({"user_id" : user})    #Document is MongoDB terminology

        if objFitbitUserDocument.count() > 0:                     #Need to update data
            for date in objFitbitAPIInstance.DATE:
                if objDatabaseInstance.FitbitData.find({"data.date": date, "user_id" : user}).count() == 0:
                    objDatabaseInstance.FitbitData.update({"user_id" : user}, {"$push" : { "data": dataFromFitbit[user][date]}})
                #Data already there, todo: updated data should be pushed
        else:                                               #fresh insertion
            for date in objFitbitAPIInstance.DATE:
                objDatabaseInstance.FitbitData.insert_one({"user_id": user, "data" : [dataFromFitbit[user][date]]})
