from vars import var
from pyrogram import  Client,filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

import logging
logging.basicConfig(level=logging.INFO)

Delevents = Client('Delete Events Bot',
                   api_id=var.API_ID,
                   api_hash=var.API_HASH,
                   bot_token=var.BOT_TOKEN
                   )

@Delevents.on_message(filters.group)
async def main(client , message):
    bot = message._client
    me = await bot.get_me()
    try:
        if message.service==True:
            whato = await message.chat.get_member(me.id)
            if whato.status=="administrator" and whato.can_delete_messages==True:
                return await message.delete()
    except Exception as e:
        print(str(e) + message.chat.id)
    


@Delevents.on_message(filters.new_chat_members & filters.group)
async def greet(client,message):
    bot = message._client
    getme = await bot.get_me()
    if message.new_chat_members:
        for i in message.new_chat_members:
            if i.id==getme.id:
                return await message.reply_text('**Thanks for Adding me Here !\n\nMake me Admin with right of Deleting Messages.\n\n@Futurecodes**')


@Delevents.on_message(filters.private & filters.command('start'))
async def pmfilter(client, message):
    me = await message._client.get_me()
    await message.reply_text("I can Delete Service Messages of Your Group,"
                             " Just Add me There as an Admin\n\n**Join @FutureCodes",
                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🔶 ADD Me 🔶",url=f"https://t.me/{me.username}?startgroup=true")]]),
                             quote=True)

@Delevents.on_message(filters.private & ~filters.command('start'))
async def okla(client,message):
    await message.delete()


@Delevents.on_message(filters.group & filters.command('start'))
async def groupo(client,message):
    await message.reply_text('Hey, I am Alive',quote=True)


Delevents.run()
hm = Delevents.get_me()
print(f"{hm.username} Deployed Successfully !!")
print("Join @FutureCodes...")
