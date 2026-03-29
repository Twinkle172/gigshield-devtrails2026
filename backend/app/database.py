from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["gigshield"]
collection = db["logs"]

def save_log(data):
    collection.insert_one(data)