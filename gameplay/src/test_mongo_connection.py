from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json # Import JSON To Handle Configuration File

# Load Configuration File
with open(r"C:\Users\ReDI User\Desktop\PythonFinalProject\gameplay\src\config.json") as config_file:
    config = json.load(config_file)
    
# Get The MongoDB URI From The COnfiguration
uri = config.get("MONGO_URI")
if not uri:
    raise ValueError("MONGO_URI is missing in the configuration file.")

# Create The MongoDB Client
client = MongoClient(uri, server_api=ServerApi("1"))

# Test MongoDB Connection
try:
    # Send A Ping To Confirm A Successful Connection
    client.admin.command("ping")
    print("Pinged Your Deployment. You Successfully Connected To MongoDB!")
except Exception as e:
    print("Error Occured:", e)