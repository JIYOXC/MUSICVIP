from ... import *
from pyrogram import *
from pyrogram.types import *
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(f"**{message.from_user.mention} لطفا اسپم نکنید و بعد از 5 ثانیه دوباره امتحان بکنید**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    if len(message.command) < 2:
        return await message.reply_text(
            "<b>لطفاً یک سطل به من بدهید تا\nجزئیات سطل را دریافت کنم !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>درحال چک کردن ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>❌ سطل اشتباه❗...</b>")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b>💠 Bin Full Details:</b>

<b>🏦 بانک:</b> <tt>{resp.bank}</tt>
<b>💳 سطل:</b> <tt>{resp.bin}</tt>
<b>🏡 کشور:</b> <tt>{resp.country}</tt>
<b>🇮🇳 پرچم:</b> <tt>{resp.flag}</tt>
<b>🧿 ISO:</b> <tt>{resp.iso}</tt>
<b>⏳ لول:</b> <tt>{resp.level}</tt>
<b>🔴 پیش پرداخت شده:</b> <tt>{resp.prepaid}</tt>
<b>🆔 تایپ:</b> <tt>{resp.type}</tt>
<b>ℹ️ فروشنده:</b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(f"""
🚫 BIN شناسایی نشد. لطفا یک BIN معتبر وارد کنید.""")
