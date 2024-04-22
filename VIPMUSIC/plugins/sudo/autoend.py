from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» جریان پایان خودکار فعال شد.\n\دستیار به طور خودکار پس از چند دقیقه هنگامی که کسی گوش نمی دهد چت ویدیویی را ترک می کند."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» جریان پایان خودکار غیرفعال شد.")
    else:
        await message.reply_text(usage)
