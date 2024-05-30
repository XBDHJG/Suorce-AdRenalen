import asyncio
from pyrogram import Client, filters ,enums
from strings.filters import command
from pyrogram.types import *
from AdRenalen import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ParseMode, ChatMemberStatus

@app.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "\n- قائمة المشرفين💘 ⋅\n— — —— — — — ——  — —\n"
    async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f" -᚜ - اليوزر ⦗ {'@'+admins.user.username if admins.user.username else admins.user.mention} ⦘.الايدي ⦗ {admins.user.id} ⦘\n"
    await message.reply(text=(admin))
