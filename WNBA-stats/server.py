from flask import request, Flask, render_template
from dotenv import dotenv_values
from pymongo import MongoClient
from seleniumDriver import BasketballDriver
import json
import league, main
import db as dbfunc

config = dotenv_values(".env")

HOST = config["HOST"]
PORT = int(config["PORT"])
app = Flask(__name__)

# Set Up DB connection
mongodb_client = MongoClient(config["MONGO_URI"])
db = mongodb_client[config["DB_NAME"]]
print("Connected to the MongoDB database!")

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/update-WNBA')
def update_league():
    WNBA_League = main.update_the_league()
    object_id = str(dbfunc.add_to_league(WNBA_League.toJSON()))
    if len(object_id):
        msg = f'Succesfully added {object_id}'
    else:
        msg = 'Error updating WNBA. Please try again.'

    return msg



    
@app.route("/add_one")
def add_one():
    pass

@app.route('/api/get_league/<string:id>')
def get_league(id):
    pass

@app.route('/api/get_team/<string:id>')
def get_team(team_name):
    pass

@app.route('/api/get_player/<string:id>')
def get_player(player_name):
    pass

if __name__ == '__main__':
    app.run(debug=True)
    mongodb_client.close()
    print("Closed app and disconnected from the MongoDB database.")

# python3 -m uvicorn server:app --reload
# c