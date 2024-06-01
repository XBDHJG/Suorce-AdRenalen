from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from AdRenalen import app
from config import OWNER_ID
from pyrogram.types import Message
from AdRenalen.utils.jarvis_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["تثبيت"], "") & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif not replied:
        await message.reply_text("**᯽︙ يرجى الرد على الرسالة التي تريد تثبيتها**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**• ثـبـتها خـلاص غور بـقـا🤨. **\n\n**الجروب:** {chat_title}\n**المشرف:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 اظهار الرساله ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command(["التثبيت"], ""))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**لا يوجد رسائل مثبته**")
    try:        
        await message.reply_text("اظهار المثبت",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 اظهار الرساله",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الغاء التثبيت"], "") & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴʟʏ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif not replied:
        await message.reply_text("**᯽︙ يرجى الرد على الرسالة التي تريد الغاء تثبيتها!**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**• رجـعـت فـڪـلامـك لـي😒. **\n\n**الجروب:** {chat_title}\n**المشرف:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 اظهار الرساله ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["حذف الصوره"], "") & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**᯽︙ جاري حذف صورة الدردشه**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("• شڪـلها معـجبتكش شيلتهالك👻.".format(message.from_user.mention))    
      except:
          await msg.edit("**᯽︙ ليس لدي أذونات كافية!**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["وضع صوره"], "") & admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("᯽︙ جاري تغيير صورة الدردش")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("`ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !`") 
      elif not reply:
           await msg.edit("**اعمل ريب علي الصوره.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("****• حـطـيتـها للـجـروب ايخدمه🌚. \nبواسطة** {}".format(message.from_user.mention))
             else:
                await msg.edit("**في مشكله جرب صوره تانيه !**")
     
          except:
              await msg.edit("**᯽︙ ليس لدي أذونات كافية!**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["وضع اسم"], "")& admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("᯽︙ جاري تغيير اسم الدردشه")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("***• حـطـيتـه للـجـروب ايخدمه🌚. \nبواسطة** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**᯽︙ ليس لدي أذونات كافية !**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**• حـطـيتـه للـجـروب ايخدمه🌚. \nبواسطة** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**᯽︙ ليس لدي أذونات كافية!**")
          

    else:
       await msg.edit("**اعمل ريب علي الاسم**")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command(["وضع وصف"], "") & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**᯽︙ جاري تغيير وصف الدردشه.**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘs!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**• حـطـيتـه للـجـروب ايخدمه🌚. \nبواسطة** {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**᯽︙ ليس لدي أذونات كافية!**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("****• حـطـيتـه للـجـروب ايخدمه🌚. \nبواسطة** {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**᯽︙ ليس لدي أذونات كافية!**")
    else:
        await msg.edit("**اعمل ريب علي الوصف!**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("غادر")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**تم المغادرة!!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #



