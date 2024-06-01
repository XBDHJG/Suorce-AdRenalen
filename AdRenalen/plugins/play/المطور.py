from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AdRenalen import app
import config

@app.on_message(filters.command("المطور", ""))
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/a802b499e948f16662dbc.jpg",
        caption="ᵂᴱᴸᶜᴼᴹᴱ ᵀᴼ ˢᴼᵁᴿᶜᴱ ᴹᴬᴿⱽᴱᴺ ༈༉",
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


