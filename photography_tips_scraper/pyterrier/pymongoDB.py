import pymongo


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["informationRetrieval"]

# Retrieve data from collections
collection1_data = list(db["data_Website1"].find())
collection2_data = list(db["data_Website2"].find())
collection3_data = list(db["data_Website3"].find())

