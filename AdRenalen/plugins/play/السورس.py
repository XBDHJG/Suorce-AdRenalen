#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅
import asyncio
from asyncio import gather
import os
import time
import requests
from pyrogram import enums
from pyrogram import types
import aiohttp
from pyrogram.types import CallbackQuery
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AdRenalen import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AdRenalen import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



##############################################################
##############################################################
          
     
@app.on_message(filters.command(["سورس","السورس","مصنع","صانع"], ""), group=221213)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9625f4182daf437e82fae.jpg",
        caption=f"""╭── • [⌯𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑⌯](https://t.me/DEV_ADRENALEN) • ──╮\n[⌯𝐒𝐔𝐏𝐏𝐔𝐑𝐓.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/BaR_AdRenalen)\n[⌯𝐂𝐇𝐀𝐍𝐍𝐄𝐋.𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/WA_AdRenalen)\n[⌯𝐁𝐎𝐓.𝐄𝐋𝐒𝐎𝐔𝐑𝐂𝐄⌯](https://t.me/Xx_MUOSIC_BOT)\n╰── • [⌯𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑⌯](https://t.me/DEV_ADRENALEN) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝐎𝐌𝐀𝐑 › ", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ›", url=f"https://t.me/WA_AdRenalen"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐔𝐏𝐏𝐔𝐑𝐓 ›", url=f"https://t.me/BAR_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.command(["حمو المرازي","حمو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/71e9ee5da45196ec2a5b0.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- حمو المرازي الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ حمو الـ مرازي 💘 ⋅ ⌯", url=f"https://t.me/H4_il"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["سحس","حسين"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f6f7e37a411a115641e56.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- حسين الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ حسين الحوب 💘 ⋅ ⌯", url=f"https://t.me/Hh_Uu_SS_Ee_Ii_Nn"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["صولو","سولو"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/81471e464fd78152dbdec.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- سولو الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ سولو الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/HA_RY2"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["فرعون","حرب"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/1d76ff4496515c122c251.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- فرعون الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ فـرعون الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/DEV_FAR3ON"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )
     


    
@app.on_message(filters.command(["عمر فيرس","فيرس"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo( 
      photo=f"https://telegra.ph/file/783c1ff05a1480c023f9e.jpg",
        caption=f"""• ⌯ 𝐓𝐇𝐄.𝐒𝐎𝐔𝐑𝐂𝐄.𝐀𝐃𝐑𝐄𝐍𝐀𝐋𝐄𝐍 ⌯ •\n- فيرس الـ شء 💘😂 ⋅""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ قناة السورس 💘 ⋅ › ", url=f"https://t.me/WA_AdRenalen"),
                ],[
                    InlineKeyboardButton(
                        "⌯ فيرس الـ تونز 💘 ⋅ ⌯", url=f"https://t.me/Xx_VAiRS_xX"), 
                    InlineKeyboardButton(
                        "⌯ ع ــمر ادرينالين 💘 ⋅ ⌯", url=f"https://t.me/DEV_ADRENALEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/Xx_MUOSIC_BOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 


##############################################################
##############################################################
##############################################################
  


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅    
