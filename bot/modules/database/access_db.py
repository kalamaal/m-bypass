import os
from bot.modules.database.database import Database

DATABASE_URL = os.environ.get("DATABASE_URL")
BOT_USERNAME = os.environ.get("BOT_USERNAME", 'don')

db = Database(DATABASE_URL, BOT_USERNAME)
