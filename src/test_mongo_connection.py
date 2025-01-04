from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
print("Current working directory:", os.getcwd())

from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()



# Check if MONGO_URI is loaded
MONGO_URI = os.getenv("MONGO_URI")
if MONGO_URI:
    print("MONGO_URI successfully loaded!")
else:
    print("Failed to load MONGO_URI from the environment variables.")
    print("Environment variables:", os.environ)

# Get the MongoDB URI from the environment variables
uri = MONGO_URI
if not uri:
    raise ValueError("MONGO_URI is missing in the environment variables.")

# Create MongoDB client
client = MongoClient(uri, server_api=ServerApi("1"))

# Test MongoDB Connection
try:
    # Send a ping to confirm a successful connection
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error occurred:", e)
