from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB URI COnnection String
uri = "mongodb+srv://MLutaaya:Satire6Digits@wordguess.cr5m5.mongodb.net/?retryWrites=true&w=majority&appName=ZuHause"

# Connect To MongoDB Client
client = MongoClient(uri, server_api=ServerApi("1"))

# Test MongoDB Connection
try:
    # Send A Ping To Confirm A Successful Connection
    client.admin.command("ping")
    print("Pinged Your Deployment. You Successfully Connected To MongoDB!")
except Exception as e:
    print("Error Occured:", e)