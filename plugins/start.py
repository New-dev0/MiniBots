from pyrogram import Client, filters

START_MSG = """
Hi, I am Auto KICK BOT

Just Add me In Chat and I will
Kick New Users Joining The Group.

Source - https://github.com/New-dev0/MiniBots

Join @FutureCodes
"""


@Client.on_message(filters.command("start"))
async def startmsg(_, message):
    await message.reply_text(START_MSG, disable_web_page_preview=True)
