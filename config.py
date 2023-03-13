from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
SUDOLIST = list(map(int, getenv("SUDOLIST", "1382938444").split()))
DATABASE = getenv("DATABASE", "database-name.db")