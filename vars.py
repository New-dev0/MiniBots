import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class var:
    API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather