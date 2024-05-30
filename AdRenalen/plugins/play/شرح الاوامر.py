#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from AdRenalen import app
from AdRenalen.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحباً بك عزيزي 𝄞</b>\n<b>» استخدم الازرار بالاسفل\n» ل تصفح اوامر الميوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامر التشغيل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامر القناة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامر الادمن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامر المطور •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "•- ع ُ مر أدرينألين 🎸 ⋅ •", url="https://t.me/DEV_AdRenalen"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحباً بك عزيزي المطور </b>\n\n<b>» استخدم الازرار بالاسفل 𝄞\n» ل تصفح اوامر الميوزك 🥁</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• التحديث •", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "• الرفع •", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "• الحظر •", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "• الاشعارات & المساعد •", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر التشغيل :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم الاغنية / رابط الاغنية)
<b>- ل تشغيل اغنية في المكالمة الصوتية</b>

فيديو + (اسم المقطع / رابط المقطع)
<b>- ل تشغيل فيديو في المكالمة المرئية</b>

بحث + الاسم
<b>- ل تحميل الاغاني والمقاطع الصوتيه من اليوتيوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر الادمن :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

الاعدادات
<b>- ل عرض إعدادات اوضاع التشغيل</b>

ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل الموسيقى في المكالمة</b>

وقف / توقف
<b>- ل إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</b>

كمل / كملي
<b>- ل إستئناف تشغيل الموسيقى في المكالمة</b>

تخطي
<b>- ل تخطي الاغنية وتشغيل الاغنية التاليه</b>

الاغاني
<b>- ل معرفة الاغاني الموجودة في قائمة الانتظار</b>

بنج
<b>- ل عرض سرعة تشغيل البوت</b>

رفع ادمن/تنزيل ادمن
<b>- ل رفع/تنزيل ادمن في البوت</b>

الادمنيه
<b>- ل عرض قائمة ادمنية البوت</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر التشغيل في القناة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفع البوت إشراف في القناة و شغل مباشر</b>
<b>- ارسل (/channelplay او ربط) + يوزر القناة ل الربط</b>
<b>- ثم استخدم الاوامر بالاسفل ل التشغيل</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + اسم الاغنية
<b>- ل تشغيل اغنية في المكالمة الصوتية</b>

فيديو + اسم المقطع
<b>- ل تشغيل فيديو في المكالمة المرئية</b>

ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل الموسيقى في المكالمة</b>

وقف / توقف
<b>- ل إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</b>

كمل / استئناف
<b>- ل إستئناف تشغيل الموسيقى في المكالمة</b>

تخطي
<b>- ل تخطي الاغنية وتشغيل الاغنية التاليه</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عدد الثواني
<b>- ل تقديم الاغنيه ل الامام</b>
/seekback + عدد الثواني
<b>- ل إرجاع الاغنيه ل الخلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر المطور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمة اوامر التحديثات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجلات
<b>- ل جلب سجلات البوت 📋</b>

تحديث
<b>- ل تحديث البوت</b>

اعاده تشغيل
<b>- ل اعادة تشغيل البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر المطور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمة اوامر الرفع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>

المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر المطور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمة اوامر الحظر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

بلوك/الغاء بلوك/المبلكين
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت</b>

احظره عام/الغاء حظره عام
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت عام</b>

المحظورين عام
<b>- ل جلب قائمة المحظورين عام في البوت</b>

حظر مجموعة/سماح
<b>- ل حظر/الغاء حظر مجموعة من استخدام ميوزك البوت</b>

المجموعات المحظورة
<b>- ل جلب قائمة بالمجموعات المحظورة من استخدام البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
● <b>قائمة اوامر المطور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمة اوامر المساعد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- ل تفعيل/تعطيل اشعارات مجموعة سجل البوت</b>

المغادره التلقائيه تفعيل/تعطيل
<b>- ل تفعيل/تعطيل المغادره التلقائيه ل الحساب المساعد من المجموعات عند عدم استخدام الميوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
   )

#𝙲𝙷.𝚂𝙾𝚄𝚁𝙲𝙴 : @WA_ADRENALEN
#𝙳𝙴𝚅 𝙰𝙳𝚁𝙴𝙽𝙰𝙻𝙴𝙽 : @DEV_ADRENALEN
#𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @BAR_ADRENALEN
#Omar AdRenalen تم التعديل بواسطة 🎸 ⋅