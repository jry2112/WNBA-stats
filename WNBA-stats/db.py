from dotenv import dotenv_values
from pymongo import MongoClient
from dotenv import dotenv_values
import league, main

config = dotenv_values(".env")

# Set Up DB connection
mongodb_client = MongoClient(config["MONGO_URI"])
db = mongodb_client[config["DB_NAME"]]
print("Connected to the MongoDB database: f{db}!")

# Add a New Item to the League Collection
def add_to_league(league_json):
    # Create the collection
    WNBA_league = db.WNBA_League
    WNBA_data = {"WNBA": league_json}
    return WNBA_league.insert_one(WNBA_data).inserted_id

# Get Name of all Leagues


# Getting an item in the League Collection

