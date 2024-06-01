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
        photo=f"https://telegra.ph/file/d7f84f3abf21196ccd7e5.jpg",
        caption=f"""╭── • [⌯𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋⌯](https://t.me/XB_DV) • ──╮\n[⌯𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨⌯](https://t.me/GGCQU)\n[⌯𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍⌯](https://t.me/SOURCE_MARVEN)\n╰── • [⌯𝐃𝐞𝐕 𝐒𝐨𝐔𝐫𝐂𝐞⌯](https://t.me/DEV_MARVEN) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ 𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋 › ", url=f"https://t.me/XB_DV"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐃𝐞𝐕 𝐍𝐚𝐑𝐮𝐓𝐨 ›", url=f"https://t.me/GGCQU"), 
                    InlineKeyboardButton(
                        "‹ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍 ›", url=f"https://t.me/SOURCE_MARVEN"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/@DffD1bot?startgroup=new"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)



@app.on_message(filters.command(["مودي","مطور السورس"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6d43ed90307453f7cbc6f.jpg",
        caption=f"""ғᴀᴄᴋ ʏᴏᴜ ʟᴏᴠᴇ ↻.""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " 𝐃𝐞𝐕 𝐌𝐨𝐨𝐃𝐲 ", url=f"https://t.me/GGCQU"),
                ],[
                    InlineKeyboardButton(
                        " ˖ 𝐃𝐞𝐕 𝐂𝐡𝐚𝐧𝐞𝐞𝐋 ˖ ", url=f"https://t.me/FPPCl"), 
                    InlineKeyboardButton(
                        " ˖ 𝐁𝐨𝐓 𝐆𝐞𝐆𝐞 ˖ ", url=f"https://t.me/GI_EGYBOT"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/GI_EGYBOT?startgroup=new"),
            ]
        ]
         ),
     )

@app.on_message(filters.command(["ديفل","مبرمج السورس"], ""), group=221212)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1ed441c02d9f8972b9e40.jpg",
        caption=f"""دمـاغـي زحـمـه م فـاضـي ،، مـتـجـيـش فـطـريـقـي عـشـان مسـوحـكـش""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " ‹ 𝐃𝐞𝐕 𝐃𝐞𝐕𝐞𝐋 › ", url=f"https://t.me/XB_DV"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝐒𝐨𝐔𝐫𝐂𝐞 𝐌𝐚𝐑𝐯𝐞𝐍 ›", url=f"https://t.me/SOURCE_MARVEN"), 
                    InlineKeyboardButton(
                        "‹ 𝐁𝐨𝐓 𝐍𝐞𝐌𝐨 ›", url=f"https://t.me/DffD1bot"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف بوت السورس الي مجموعتك ⚡️🎸 ⋅ ›", url=f"http://t.me/DffD1bot?startgroup=new"),
            ]
        ]
         ),
     )
        

@app.on_message(filters.command(["اسمي","اسمي اي","قول اسمي"], ""), group=123222)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- اسمك » ⦗ {message.from_user.mention} ⦘ 💘 ⋅""") 

pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ChatMemberStatus


iddof = []
@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "")& filters.group)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("**الامر معطل من قبل .**")
      iddof.append(message.chat.id)
      return await message.reply_text("**تم تعطيل الايدي بنجاح .**")
   else:
      return await message.reply_text("**عذرا عزيزي هذا الامر للادمن الجروب فقط .**")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "")& filters.group)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("**الايدي مفعل من قبل .**")
      iddof.remove(message.chat.id)
      return await message.reply_text("**تم تفعيل الايدي بنجاح .**")
   else:
      return await message.reply_text("**عذرا عزيزي هذا الامر للادمن الجروب فقط .**")

@app.on_message(filters.command(["ايدي", "ا"], ""))
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("**تم تعطيل امر الايدي من قبل المشرفين .**")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not id.get(message.from_user.id):
         id[user.id] = []
       idd = len(id[user.id])
       await message.reply_photo(photo=photo, caption=f"**name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bio}**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 💋", callback_data=f"heart{user_id}")],]),)
            


id = {}
@app.on_callback_query(filters.regex("kiss"))  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("kiss")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in id[usr.id]:
         id[usr.id].append(query.from_user.mention)
    else:
         id[usr.id].remove(query.from_user.mention)
    idd = len(id[usr.id])
    await query.edit_message_text(f"**name : {usr.first_name}\nid : {usr.id}\nuser : [@{usr.username}]\nbio : {usr.bio}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 💋", callback_data=f"heart{usr.id}")]])
##############################################################
##############################################################
##############################################################
  


#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅    
