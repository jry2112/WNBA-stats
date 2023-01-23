from flask import request, Flask, render_template
from dotenv import dotenv_values
from pymongo import MongoClient

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



if __name__ == '__main__':
    app.run(debug=True)
    mongodb_client.close()
    print("Closed app and disconnected from the MongoDB database.")

# python3 -m uvicorn server:app --reload
# http://127.0.0.1:8000/