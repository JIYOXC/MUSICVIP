import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC import app
from datetime import datetime
from VIPMUSIC.utils.database import get_assistant
# Assuming Userbot is defined elsewhere

last_checked_time = None

@app.on_message(filters.command("botschk") & filters.group)
async def check_bots_command(client, message):
    global last_checked_time
    try:
        # Start the Pyrogram client
        userbot = await get_assistant(message.chat.id)

        # Get current time before sending messages
        start_time = datetime.now()

        # Extract bot username from command
        command_parts = message.command
        if len(command_parts) == 2:
            bot_username = command_parts[1]
            response = ""  # Define response variable
            try:
                bot = await userbot.get_users(bot_username)
                bot_id = bot.id
                await asyncio.sleep(0.5)
                await userbot.send_message(bot_id, "/start")
                await asyncio.sleep(3)
                # Check if bot responded to /start message
                async for bot_message in userbot.get_chat_history(bot_id, limit=1):
                    if bot_message.from_user.id == bot_id:
                        response += f"╭⎋ {bot.mention}\n l\n╰⊚ **وضعیت: آنلاین ✨**\n\n"
                    else:
                        response += f"╭⎋ [{bot.mention}](tg://user?id={bot.id})\n l\n╰⊚ **وضعیت: آفلاین ❄**\n\n"
            except Exception:
                response += f"╭⎋ {bot_username}\n l\n╰⊚ **یا نام کاربری اشتباهی داده اید وگرنه به دلیل محدودیت نمی توانم بررسی کنم. **\n\n"
            # Update last checked time
            last_checked_time = start_time.strftime("%Y-%m-%d")
            await message.reply_text(f"{response}⏲️ ʟᴀsᴛ ᴄʜᴇᴄᴋ: {last_checked_time}")
        else:
            await message.reply_text("فرمت دستور نامعتبر.\n\nخواهش می کنم استفاده کنید /botschk Bot_Username\n\nʟɪᴋᴇ :- `/botschk @FullMusicKingbot`")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /botschk command: {e}")
    
