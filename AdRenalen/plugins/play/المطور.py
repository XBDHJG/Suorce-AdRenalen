from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from ANNIEMUSIC import app
import config

@app.on_message(filters.command("المطور", ""))
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/5c00f6afa2b6266710065.jpg",
        caption="𝖶𝖤𝖫𝖢𝖮𝖬𝖤 𝖳𝖮 𝖲𝖮𝖴𝖱𝖢𝖤 𝖬𝖠𝖱𝖵𝖤𝖭",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة البوت . ", url=f"https://t.me/SOURCE_MARVEN"
                    ),
                ],
            ]
        ),
    )

