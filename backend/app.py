from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # habilita cors

MONGO_HOST = os.environ.get("MONGO_HOST", "mongo")
MONGO_PORT = 27017
client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
db = client["mydatabase"]
collection = db["formdata"]

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Data saved to MongoDB!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
