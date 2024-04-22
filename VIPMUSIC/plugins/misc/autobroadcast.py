import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else False

START_IMG_URLS = "https://variety.com/wp-content/uploads/2022/07/Music-Streaming-Wars.jpg?w=1000&h=563&crop=1&resize=1000%2C563"




BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ Click & join ๏", url=f"https://t.me/Securit_y_Breach")
        ]
    ]
)

MESSAGE = f"""**๏ این ربات پخش کننده موزیک پیشرفته برای گروه ها و کانال تلگرام است. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ خوش آمدگویی پشتیبانی شده - اطلاعیه سمت چپ، تگال، برچسب موسیقی پادشاه، ممنوعیت - بی صدا، لوریک، آهنگ - دانلود ویدیو و غیره ❤️

🔐استفاده کنید » [/start](https://t.me/{app.username}?start=help) برای برسی ربات

➲ ربات :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏", url=f"https://t.me/FullMusicKingbot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**پخش خودکار فعال است بنابراین پخش خودکار/پخش در تمام چت ها به طور مداوم انجام می شود **\n**می توان آن را با قرار دادن  متغیر متوقف کرد [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (خالی بمان و چیزی ننویس)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URLS, caption=caption, reply_markup=BUTTONS)
                    await asyncio.sleep(20)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
