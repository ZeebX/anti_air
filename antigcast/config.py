import os
import logging
from logging.handlers import RotatingFileHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6936605005:AAGylSU8pF84dUMzMXm0QpmyXHcFkbzPrco")
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

APP_ID = int(os.environ.get("APP_ID", "26724473"))
API_HASH = os.environ.get("API_HASH", "7bc7d1f9b2f3d3f1bfd272db56ac0ba1")

LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1002009684047"))

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://Xyxx:Helmi4636@cluster0.9yy5ve9.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Xyxx")
BROADCAST_AS_COPY = True

PLUG = dict(root="antigcast/plugins")

OWNER_ID = [int(x) for x in (os.environ.get("OWNER_ID", "940232666").split())]
OWNER_NAME = os.environ.get("OWNER_NAME", "Dante")


LOG_FILE_NAME = "antigcast_logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

CREATOR = [
    940232666, # p
]

