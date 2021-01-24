import os
from vars import var
from pyrogram import  Client,filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

import logging
logging.basicConfig(level=logging.WARNING)

Telescopy = Client('Telescopy Bot',
                   api_id=var.API_ID,
                   api_hash=var.API_HASH,
                   bot_token=var.BOT_TOKEN
                   )

def checksquare(message):
    if message.video:
        okla=message.video
    else:
        okla=message.animation
    if okla.height / okla.width == 1:
        return True
    else:
        return False


@Telescopy.on_message(filters.video | filters.animation)
async def main(client , message):
    chck = checksquare(message)
    if chck==True:
        dnl=await message.download()
        await message.reply_video_note(dnl,quote=True)
        os.remove(dnl)
    else:
        await message.reply_text('**Please Send me Square Video or Gif...**',quote=True)

                                      

@Telescopy.on_message(filters.new_chat_members & filters.me)
async def greet(client,message):
    await message.reply_text('**Thanks for Adding me Here !\n\nI will Convert Square Videos or Gif When they will be send in this Chat**',
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📣 Support Group 📣",url="https://t.me/FutureCodes")]]))


@Telescopy.on_message(filters.private & filters.command('start'))
async def pmfilter(client, message):
    await message.reply_text("**I can Convert Square Video or Gif to Circle Form...\n\nJust send me Square Video or Gif\n\nJoin @FutureCodes**",
                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🌟 Support Group 🌟",url=f"https://t.me/FutureCodes")]]),
                             quote=True)


@Telescopy.on_message(filters.group & filters.command('start'))
async def groupo(client,message):
    await message.reply_text('Hi, I am Alive',quote=True)


Telescopy.run()
hm = Telescopy.get_me()
logging.print(f"{hm.username} Deployed Successfully !!")
logging.print("Join @FutureCodes...")
