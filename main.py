import logging
from pyrogram import Client, idle
from vars import Var

logging.basicConfig(level=logging.WARNING)


Client = Client(
    "Auto-Kick Bot",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)


Client.start()
US = Client.get_me()
print(f"@{US.username} Deployed Successfully !")

idle()
