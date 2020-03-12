# Importing PyMongo for accessing MongoDB
import pymongo

# Establishing the Connection to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["OMDB_movies_db"]
mycol = mydb["my_OMDB_collection"]


# Accessing Tweets from MongoDB
for x in mycol.find():
  print(x) 