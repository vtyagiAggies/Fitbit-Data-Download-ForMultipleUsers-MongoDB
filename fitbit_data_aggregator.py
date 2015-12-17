#!/usr/bin/python
from pymongo import MongoClient
import authenticate_and_fetch_fitbit_data

if __name__ == "__main__":
    #Setting up MongDB connection and database: DevicesData & collection: FitbitData
    mongoDbClient = MongoClient()
    objDatabaseInstance = mongoDbClient.DevicesData
    objFitbitCollection = objDatabaseInstance.FitbitData.find()
    for document in objFitbitCollection:
        print document

    #Getting data from fitbit
    users = ["diabetesresearchtamu@gmail.com"]
    objFitbitAPIInstance = authenticate_and_fetch_fitbit_data.AuthenticateAndFetchFitbitData()
    data = objFitbitAPIInstance.getData(users)

    print data


    for user in users:
        objFitbitUserDocument = objDatabaseInstance.FitbitData.find()    #Document is MongoDB terminology