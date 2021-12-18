import asyncio
import sys

from motor import motor_asyncio
from MashaRoBot import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from MashaRoBot.conf import get_int_key, get_str_key
from MashaRoBot import LOGGER

MONGO_PORT = 27017
MONGO_DB_URI = 
MONGO_DB = "Lovely"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["MashaRoBot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(LOGGER.critical("Can't connect to mongodb! Exiting..."))
