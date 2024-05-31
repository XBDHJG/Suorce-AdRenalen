import asyncio
from pyrogram import Client, filters
from strings.filters import command
from AdRenalen.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️☺️!"




REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
        ("الاوامر")
    ],
    
        [
        ("صوره"),
        ("اقتباس")
    ],
        ("مبرمج السورس"),
    ],
    [
        ("مطور السورس"),
    ],
    [
        ("استوري"),
        ("كت")
    ],
    [
        ("اسالني"),
        ("بايو")
    ],
    [
        ("قران"),
        ("حروف")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("نكته"),
        ("حكمه")
    ],
    [
        ("انصحني")
    ],
    [
        ("لو خيروك"),
        ("حساب العمر")
    ],    
    [
        ("اقفل الكيب")
    ]
  
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اقفل الكيب"))
async def down(client, message):
          m = await message.reply("تم قفل الكيب بنجاح 💘 ⋅ ", reply_markup= ReplyKeyboardRemove(selective=True))

