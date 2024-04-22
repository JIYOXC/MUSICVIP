from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ Help ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✡ گروه ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💠 منو به گروه جدیدت اضافه بکن 💠",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="گروه✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="درباره ما🥀", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="۞ ویژگی ها ۞", callback_data="settings_back_helper")
        ],
    ]
    return buttons
