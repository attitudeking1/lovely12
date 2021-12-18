# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/MashaRoBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 2628603  # integer value, dont use ""
    API_HASH = "fa20340c1f260a2b805dbf3dac0454c2"
    TOKEN = "1777728008:AAEm-5a6gVrzpjoLbL4TBTOMC5UavOpC-bM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1642113657  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "TUSHAR204"
    SUPPORT_CHAT = "LOVELYAPPEAL"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001253661229
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001426207683
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database module
    REDIS_URI = "redis://:v78Q3dEJaVQRT9LR1EbDilgEGdWvnopV@redis-15390.c259.us-central1-2.gce.cloud.redislabs.com:15390/Lovely" # Get One From RedisLabs.com Make Role And Database Make Sure that the Format Of Url Should be: 'redis://Username:pass@endpoint/dbname'
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1378449566 2097082001 2072357336 2136080200 1926801217 936481432"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1217888448 1677365574 1997387632 1962664022 1270127834 1521131774 1747260012 2069298636 2128441506 2102677065 2105860670 5032100535 5036020547"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "2034973894 1944766409 2070469162 1964362058 2007701745 1669178360 1902787452 1872917918 1618246574 2019281390 2115851613 2068551800 2132027598 1901951380 2030474884 1812558111"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1642113657 1677365574"
    WOLVES = "1642113657 1677365574" 
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "HS5OR9E34VX1SA8Q"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "IUHUQBIOU1T9"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        " "  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
