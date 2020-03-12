# importing pymongo for feeding OMDB_movies in MongoDB
from pymongo import MongoClient
import json

# Eastablishing the Connection 
db_client = MongoClient('localhost', 27017)

# Creating a Fresh Database for Storing OMDB_movies
db = db_client['OMDB_movies_db']

# Creating a Fresh Collection which acts analogous to a table in Relational DBMS
OMDB_movies_Collection = db['my_OMDB_collection']


# Importing OMDB_movies from JSON file into a list of dictionaries
OMDB_movies = []
for line in open('Extracted_OMDB_Data.json', 'r'):
    OMDB_movies.append(json.loads(line))


# Refershing the Collection Values
OMDB_movies_Collection.remove()

# Stotring the OMDB_movies into MongoDB
result = OMDB_movies_Collection.insert_many(OMDB_movies)


# Closing the MongoDB Connection
db_client.close()