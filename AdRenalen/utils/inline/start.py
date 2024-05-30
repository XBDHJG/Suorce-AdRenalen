from pyrogram.types import InlineKeyboardButton

import config
from AdRenalen import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي جروبك او قناتك 🎸 ⋅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الاوامر 🎸 ⋅", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="المطور 🎸 ⋅", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس 🎸 ⋅", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="- مـبـرمجـيـن الـسـورس 🎸 ⋅", url=f"https://t.me/DEV_MARVEN"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي جروبك او قناتك 🎸 ⋅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الاوامر 🎸 ⋅", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="المطور 🎸 ⋅", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس 🎸 ⋅", url=config.SUPPORT_CHANNEL),
        ],
        [
         
            InlineKeyboardButton(text="- مـبـرمجـيـن الـسـورس 🎸 ⋅", url=f"https://t.me/DEV_MARVEN"),
        ],
    ]
    return buttons
