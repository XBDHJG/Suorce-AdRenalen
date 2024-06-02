from pyrogram import Client, filters, enums
import asyncio
from AdRenalen import app


@app.on_message(filters.command("مسح الروابط", prefixes="") & filters.group)
async def del_urls(bot, msg):
    await msg.reply("• جاري جلب الروابط ..")
    num = 0
    async for message in bot.search_messages(msg.chat.id, filter=enums.MessagesFilter.URL):
        try:
            await message.delete(revoke=True)
            num += 1
        except:
            pass
    await msg.edit(f"• تم مسح {num} رساله تحتوي علي روابط")
    
    
@app.on_message(filters.command("مسح الصور", prefixes="") & filters.group)
async def del_photos(bot, msg):
    await msg.reply("• جاري جلب الصور ..")
    num = 0
    async for message in bot.search_messages(msg.chat.id, filter=enums.MessagesFilter.PHOTO):
        try:
            await message.delete(revoke=True)
            num += 1
        except:
            pass
    await msg.edit(f"• تم مسح {num} رساله تحتوي علي صور")
    
    
@app.on_message(filters.command("مسح الفيديوهات", prefixes="") & filters.group)
async def del_videos(bot, msg):
    await msg.reply("• جاري جلب الفديوهات ..")
    num = 0
    async for message in bot.search_messages(msg.chat.id, filter=enums.MessagesFilter.VIDEO):
        try:
            await message.delete(revoke=True)
            num += 1
        except:
            pass
    await msg.edit(f"• تم مسح {num} رساله تحتوي علي الفديوهات")    
    
    
@app.on_message(filters.command("مسح الملصقات", prefixes="") & filters.group)
async def del_stickers(bot, msg):
    await msg.reply("• جاري جلب الملصقات ..")
    num = 0
    async for message in bot.search_messages(msg.chat.id, filter=enums.MessagesFilter.STICKER):
        try:
            await message.delete(revoke=True)
            num += 1
        except:
            pass
    await msg.edit(f"• تم مسح {num} رساله تحتوي علي الملصقات")    
    
       