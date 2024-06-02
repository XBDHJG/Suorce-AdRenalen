from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AdRenalen import app
import config

@app.on_message(filters.command("المطور", ""))
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/d614c73c61ae132773756.png",
        caption="𝖜𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖘𝖔𝖚𝖗𝖈𝖊 𝖗𝖊𝖆𝖑",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة السورس . ", url=f"https://t.me/SOURCE_MARVEN"
                    ),
                ],
            ]
        ),
    )

