import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.utils.database import get_assistant
from VIPMUSIC.utils.database import delete_served_chat

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)
        
        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = message.from_user.mention if message.from_user else "کاربر ناشناس"
            title = message.chat.title
            username = f"@{message.chat.username}" if message.chat.username else "چت خصوصی"
            chat_id = message.chat.id
            left = f"✫ <b><u>#لفت_گروه</u></b> ✫\n\nعنوان چت : {title}\n\nشناسه چت : {chat_id}\n\nحذف شده توسط : {remove_by}\n\nربات : @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        print(f"Error: {e}")
    
