from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["gigshield"]
users_collection = db["users"]
plans_collection = db["plans"]
policies_collection = db["policies"]
claims_collection = db["claims"]
logs_collection = db["logs"]

def create_user(user_data):
    user_data["created_at"] = datetime.utcnow()
    return users_collection.insert_one(user_data)

def get_user(user_id):
    return users_collection.find_one({"_id": user_id})

def create_plan(plan):
    return plans_collection.insert_one(plan)

def get_plans():
    return list(plans_collection.find())

def create_policy(policy):
    policy["created_at"] = datetime.utcnow()
    return policies_collection.insert_one(policy)

def create_claim(claim):
    claim["status"] = "PENDING"
    claim["created_at"] = datetime.utcnow()
    return claims_collection.insert_one(claim)

def update_claim_status(claim_id, status):
    return claims_collection.update_one(
        {"_id": claim_id},
        {"$set": {"status": status}}
    )

def save_log(data):
    data["timestamp"] = datetime.utcnow()
    logs_collection.insert_one(data)

