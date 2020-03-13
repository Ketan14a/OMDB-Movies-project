# Importing PyMongo for accessing MongoDB
import pymongo

# Establishing the Connection to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["OMDB_movies_db"]
mycol = mydb["my_OMDB_collection"]


# Accessing Tweets from MongoDB
for x in mycol.find():
  print("Title:"+ x['Title']) 
  print("Year:"+ str(x['Year']))
  print("IMDB_ID:"+x['IMDB_ID'])
  print("Type:"+x['Type'])
  print("Genre:"+x['Genres'])
  print("Plot:"+x['Plots'])
  print("IMDB Ratings:"+x['IMDB_ratings'])
  print("Awards:"+ x['Awards'])
  print()
  print()