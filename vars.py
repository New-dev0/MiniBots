from decouple import config


class Var:
    API_ID = config("API_ID", default=6)  # from https://my.telegram.org/apps
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")  # from https://my.telegram.org/apps
    BOT_TOKEN = config("BOT_TOKEN")  # from @botfather
