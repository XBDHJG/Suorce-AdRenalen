#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅

from pyrogram import filters, Client
from AdRenalen import app
import asyncio
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AdRenalen.core.call import Omar
from AdRenalen.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)

@app.on_message(filters.regex("^مين في الكول$|^مين ف الكول$|^الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Omar,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./AdRenalen/assets/AdRenalen_Call.mp3"), stream_type=StreamType().pulse_stream)
        text="- الحبايب الي ف الكول 🎸 ⋅\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="بيتكلم 🗣"
            else:
                mut="ساكت 🔕"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k} : {user.mention} : {mut}\n"
        text += f"\nعددهم : {len(participants)}"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"سلامت نظرك الكول مش مفتوح اصلا 😂💘 ⋅")
    except TelegramServerError:
        await message.reply(f"يوجد خطأ ارجو المحاولة بعد دقيقة 🎸 ⋅")

    except AlreadyJoinedError:
        text="- الحبايب الي ف الكول 🎸 ⋅\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣"
            else:
                mut="ساكت 🔕"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k} : {user.mention} : {mut}\n"
        text += f"\nعددهم : {len(participants)}"    
        await message.reply(f"{text}")
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("الكول اتفتح هيرغو ويصدعونا بقا 😂💘 ⋅")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"تم انهاء مكالمة الفيديو مدتها {da} ثواني 🎸 ⋅")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f" تم انهاء مكالمة الفيديو مدتها دقيقه 🎸 ⋅")
        elif 2 <= ma[0] < 3:
            await message.reply(f" تم انهاء مكالمة الفيديو مدتها دقيقتين 🎸 ⋅")
        elif 3 <= ma[0] < 11:
            await message.reply(f"تم انهاء مكالمة الفيديو مدتها {ma[0]} دقايق 🎸 ⋅")  
        else:
            await message.reply(f"تم إنهاء مكالمة الفيديو مدتها {ma[0]} دقيقه 🎸 ⋅")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"تم انهاء مكالمة الفيديو مدتها ساعه 🎸 ⋅")
        elif 2 <= ho[0] < 3:
            await message.reply(f"تم انهاء مكالمة الفيديو مدتها ساعتين 🎸 ⋅")
        elif 3 <= ho[0] < 11:
            await message.reply(f"تم انهاء مكالمة الفيديو مدتها {ho[0]} ساعات 🎸 ⋅")  
        else:
            await message.reply(f"تم إنهاء مكالمة الفيديو مدتها {ho[0]} ساعة 🎸 ⋅")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"تم انهاء مكالمة الفيديو مدتها يوم 🎸 ⋅")
        elif 2 <= day[0] < 3:
            await message.reply(f" تم انهاء مكالمة الفيديو مدتها يومين 🎸 ⋅")
        elif 3 <= day[0] < 11:
            await message.reply(f" تم انهاء مكالمة الفيديو مدتها {day[0]} ايام 🎸 ⋅")  
        else:
            await message.reply(f" تم إنهاء مكالمة الفيديو مدتها {day[0]} يوم 🎸 ⋅")
            
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"- قام ›› ⦗ {message.from_user.mention} ⦘ 😂💘 ⋅"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n- بدعوة ›› ⦗ {user.mention} ⦘ 😂💘 ⋅"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  

             
             
#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅
