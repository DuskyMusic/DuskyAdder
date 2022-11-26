from pyrogram import Client, filters 
from pyrogram.types import Message
from config import SUDO_USERS
import asyncio

Boom = SUDO_USERS

@Client.on_message(filters.command(["inviteall", "kidnapall", "hack"], [".", "!", "/"]) & filters.user(SUDO_USERS))
async def inviteall(client: Client, message: Message):
    Dusky = await message.reply_text("⚡  Title also\n ex: /DuskyAdder @Tamilchatting_Tamil_Group")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await hmf.edit_text(f"Getting users from {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()
