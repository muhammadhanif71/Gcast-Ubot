from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


class Var:
    API_HASH = getenv("API_HASH")
    API_ID = int(getenv("API_ID", ""))
    ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/557efb9e89c45d02e9913.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hey, Saya Gcast Ubot Dibuat dengan basis pyrogram versi terbaru")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283, -1001601365018]
    LOG_CHAT = int(getenv("LOG_CHAT") or 0)
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    DB_URL = getenv("DATABASE_URL", "")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Stuf-Userbot:Stuf-Userbot@stuf-userbot.eugqicq.mongodb.net/?retryWrites=true&w=majority")
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "WEnHwQnst3E2HzjGgwmy4UpB")
    STRING_1 = getenv("STRING_1", "")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
