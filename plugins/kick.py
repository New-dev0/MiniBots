from pyrogram import Client, filters


MY_JOIN = """Thanks for Adding Me !
Auto Kicks are Now Active in This Chat!"""

CHAT_ID = []


@Client.on_message(filters.new_chat_members)
async def kickpy(_, message):
    me = await message._client.get_me()
    for mem in message.new_chat_members:
        if mem.id == me.id:
            return await message.reply_text(MY_JOIN)
        try:
            await message.chat.kick_member(mem.id)
        except Exception as e:
            if message.chat.id in CHAT_ID:
                return
            await message.reply_text(str(e))
            CHAT_ID.append(message.chat.id)
