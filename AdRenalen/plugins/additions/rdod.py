import asyncio
import random
from AdRenalen import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import filters, Client

@app.on_message(filters.text, group=57355566)
async def d5on(client, message):
   if message.text == "عندك كام سنه":
       await message.reply_text(f"لا قول انت الاول 😂❤️")
   elif message.text == "حبك":
       await message.reply_text(f" نا عايز مح انا كمان 🥺💔")
   elif message.text == "حصلخير":
       await message.reply_text(f"حصلخير اي هيجي منين الخير وانت هنا. 🙂😂")
   elif message.text == "خدو مني الفون":
       await message.reply_text(f"كلميني ع الواتس يمزه 😂❤️")
   elif message.text == "حه":
       await message.reply_text(f"اي يستا جيت ع الجرح 🙂😂")
   elif message.text == "بابا":
       await message.reply_text(f"😂❤️ مين حبيب بابا انا مين روح بابا انا نينينيني")
   elif message.text == "ماما":
       await message.reply_text(f"ست الحبايب ياحبيه ياحبيبه 😌😂")
   elif message.text == "شتمني":
       await message.reply_text(f"ولا حاجه يقلبي بكرا يتزنق ويجي حقك من غير متقل ادبك 😂❤️ مصيبه ده")
   elif message.text == "يبرو":
       await message.reply_text(f"اي يقلب البرو في حد مزعلك انا هقوم بالواجب 😂❤️")
   elif message.text == "يسطا":
       await message.reply_text(f"قابلتك ع البسطه 😂❤")
   elif message.text == "فرحان":
       await message.reply_text(f"❤️ ربنا يتمم افراحك")
   elif message.text == "عيب":
       await message.reply_text(f"سيب الواد يلعب 😂😂")
   elif message.text == "يحب":
       await message.reply_text(f"🥺❤️ اي ياكبد الحب")
   elif message.text == "عامل اي":
       await message.reply_text(f"الحمدلله وانت 🥺❤️")
   elif message.text == "بعشقك":
       await message.reply_text(f"وه وه قدام الناس كده عيب 🙈❤️")
   elif message.text == "انت نرم":
       await message.reply_text(f"الله يرحم ابوك كان بيشرب الشربه بخرطوم الغساله😂🙂")
   elif message.text == "خد":
       await message.reply_text(f"لا يعم نا ماشي سلام 🌝😂")
   elif message.text == "الزعامه":
       await message.reply_text(f"الزعامه فوق وكسكلياه ضالابواه 💔😹")
   elif message.text == "فين الادمن":
       await message.reply_text(f"ايش بتريد منه🤔")
   elif message.text == "هاي":
       await message.reply_text(f"هاى ماى جايز❤️😉")
   elif message.text == "هلو":
       await message.reply_text(f"هلو باللى سرق قلبى 🤗🌟")
   elif message.text == "ماشى":
       await message.reply_text(f"ماشى رايح فين ❤️🥺")
   elif message.text == "غلس":
       await message.reply_text(f"اهو انت💔🥺")
   elif message.text == "انت مين":
       await message.reply_text(f"بتسال لي💨🌝")
   elif message.text == "احبك":
       await message.reply_text(f"مسمعكش تقولي كده تانى 🙂")
   elif message.text == "اوف":
       await message.reply_text(f"لمين هاي ؟🌚🌙")
   elif message.text == "في اي":
       await message.reply_text(f"مافيش حاجه🙄")
   elif message.text == "نايمين":
       await message.reply_text(f"انا سهران😿😹")
   elif message.text == "كفايه كلام":
       await message.reply_text(f"اسكت انت😼👊")
   elif message.text == "هيي":
       await message.reply_text(f"يالا ياض من هنا😂💔")
   elif message.text == "انت فين":
       await message.reply_text(f"بارض الله الواسعه 😽😂")
   elif message.text == "😂😂😂":
       await message.reply_text(f"تدوم يغالى 💘🙄")
   elif message.text == "هه":
       await message.reply_text(f"ضحكه مش سالكه 😳😂")
   elif message.text == "البوت عطلان":
       await message.reply_text(f"بطلو كدب بقي 🙄🙂")
   elif message.text == "البوت واقف":
       await message.reply_text(f"لا تكذب حبي🌞")
   elif message.text == "المدرسه":
       await message.reply_text(f"اذا بتجيب اسمها بطردك🌞✨")
   elif message.text == "شوف":
       await message.reply_text(f"اشوف اي 🌝🌝")
   elif message.text == "🌝":
       await message.reply_text(f"حبعمري😽💚")
   elif message.text == "🙂":
       await message.reply_text(f"هنكد بقا اهو 😕")
   elif message.text == "🚶💔":
       await message.reply_text(f"تعالي اشكيلي ايش فيك🙁💔")
   elif message.text == "🙁":
       await message.reply_text(f"اشكيلي هموك ليش متضايق🙁💔")
   elif message.text == "🙁":
       await message.reply_text(f"اشكيلي هموك ليش متضايق🙁💔") 
   elif message.text == "😳":
       await message.reply_text(f"اوميقد😐😹")
   elif message.text == "😒":
       await message.reply_text(f"ايش بيك ؟😟")   
   elif message.text == "🌚":
       await message.reply_text(f"فديتك هاي🙊👄")
   elif message.text == "تحبني":
       await message.reply_text(f"اممم افكر🙁😹") 
   elif message.text == "بتحبني":
       await message.reply_text(f"وهو القمر ميتحبش ؟؟ ❤️😂")
   elif message.text == "باي":
       await message.reply_text(f"ع فين لوين رايح وسايبنى🙁💔")
   elif message.text == "تعالي خاص":
       await message.reply_text(f"لو بنت هاجي غير كدة لا 🙄😂")
   elif message.text == "فرخه":
       await message.reply_text(f"خليها تبيض😂😂😂")
   elif message.text == "حاضر":
       await message.reply_text(f"حضرلك الخير ياارب ❤️")
   elif message.text == "😐":
       await message.reply_text(f"شطووور 🙂")
   elif message.text == "ار يو ريدى":
       await message.reply_text(f"بكوى القميص وجهزت اهو 🔥🥺😂") 
   elif message.text == "وات":
       await message.reply_text(f"ازغط بط 😳😂")
   elif message.text == "ملكش دعوة":
       await message.reply_text(f"خدو واستعوى ❤️😂")   
   elif message.text == "انت مالك":
       await message.reply_text(f"مالى فى جيبى هه ❤️😂")
   elif message.text == "احسن":
       await message.reply_text(f"جتك لحسه 😂💃") 
   elif message.text == "نعم":
       await message.reply_text(f"نعم الله عليك🙂")
   elif message.text == "نرتبط":
       await message.reply_text(f"مرتبط مع نفسي واحزاني ❤️😢")
   elif message.text == "بلوك":
       await message.reply_text(f"لما اللي منك يجرحك😢") 
   elif message.text == "انا بكرهك":
       await message.reply_text(f"حبني بلييز 🥺")
   elif message.text == "بيبى":
       await message.reply_text(f"قلبى ياناس قلباااااى 😂❤️")   
   elif message.text == "ها":
       await message.reply_text(f"هاا ياروحي")
   elif message.text == "فديت":
       await message.reply_text(f"فدااك ♥️") 
   elif message.text == "محدش بيسال علي":
       await message.reply_text(f"بنسأل عليك ياحلووو 🖤🔍")
   elif message.text == "شلونكم":
       await message.reply_text(f"تمام وانت يكيوت ؟ 💕")
   elif message.text == "كداب":
       await message.reply_text(f"انت اللى كدااب يحليتها ❤️😹") 
   elif message.text == "عادي":
       await message.reply_text(f"فى المعادى هه😂😂") 
   elif message.text == "عجبتك":
       await message.reply_text(f"اكييد اكتيير 😎") 
   elif message.text == "حبيبي":
       await message.reply_text(f"اوه ياه 🌝😂") 
   elif message.text == "بت":
       await message.reply_text(f"ليا اسم ياض يعره يمهزء نينينينني😹😎🏃🏻‍♀") 
   elif message.text == "روحي":
       await message.reply_text(f"خلصتت روحكك يبعيد😹🚶🏻‍♀💔") 
   elif message.text == "بوتي":
       await message.reply_text(f"قلب بوتكك من جواا 🥺♥️") 
   elif message.text == "مش هتيجي":
       await message.reply_text(f"مش هرووووح 😹🏃🏻‍♀🏃🏻‍♀") 
   elif message.text == "تف":
       await message.reply_text(f"اصفخص عليك منتن ءتفووووو😹👅") 
   elif message.text == "وه":
       await message.reply_text(f"بسيفلاح يعره مسمعش صوتكك😹🤸🏻‍♀🙊") 
   elif message.text == "اي":
       await message.reply_text(f"جتك اوهه م سامع ولا ايي😹👻") 
   elif message.text == "طيب":
       await message.reply_text(f"فرح خالتك قريب😹💋💃🏻") 
   elif message.text == "خلاص":
       await message.reply_text(f"خلصتت روحكك يبعيد😹🚶🏻‍♀💔") 
   elif message.text == "مراتي":
       await message.reply_text(f"عرفني عليها ينوبك ثواب🥺🙈") 
   elif message.text == "يوتكه":
       await message.reply_text(f"بتعاكس انت لحد ميقولو عليك حكاك بتحصل بتحصل 🙂😂") 
   elif message.text == "يمزه":
       await message.reply_text(f"خف معاكسه يبني عييب 🙂😂") 
   elif message.text == "حلال":
       await message.reply_text(f"الله عليك ياشيخنا 🙄😹") 
   elif message.text == "حرام":
       await message.reply_text(f"اخيرا في حد عاقل ❤️🙈") 
   elif message.text == "سجاره":
       await message.reply_text(f"ابوك عارف انك بتشرب سجاير 😂🙂") 
   elif message.text == "ينرم":
       await message.reply_text(f"عييب مشوفتش نفسك لم اول مره مسكت تلفون كان منظرك كده 🤪") 
   elif message.text == "حبيبتي":
       await message.reply_text(f"اوعه ع الجمدان بقا حبيبتي وشغل عالي 🙈❤️") 
   elif message.text == "سي في":
       await message.reply_text(f"كفايه شقط يبني سيب حاجه لغيرك 😹👅") 
   elif message.text == "اخرس":
       await message.reply_text(f"هتت لازقه وحطها ع بوئيي😹🙊🤸🏻‍♀") 
   elif message.text == "بقولك":
       await message.reply_text(f"لاء متقولش نينينينني😹🏃🏻‍♀♥️")    
   elif message.text == "ده بوت":
       await message.reply_text(f"ياحلولي هو كان فاكرني انسان ولا ايي 😹") 
   elif message.text == "جيت":
       await message.reply_text(f"لف وارجع تاني م حوارر 😹🚶🏻‍♀♥️") 
   elif message.text == "سالخير":
       await message.reply_text(f"سالنور ياولا 💃🏻😹") 
   elif message.text == "احتويه":
       await message.reply_text(f"✓ تم احتواء العضو بنجاح \n ✓ تع ف حضن حمو ياولا 😹♥️") 
   elif message.text == "يوه":
       await message.reply_text(f"يقطعني 😹🙆🏻‍♀♥️") 
   elif message.text == "ششش":
       await message.reply_text(f"بنهش كتاكيت احنا هنا ولا اى😒💔") 
   elif message.text == "صباح الخير":
       await message.reply_text(f"صباحك عسل ي عسل❤️🙄") 
   elif message.text == "روم اي ده":
       await message.reply_text(f"هيكون اى يعني غير رغى🙄😂") 
   elif message.text == "اسكت":
       await message.reply_text(f"اما انت غتت صحيح💔🥺") 
   elif message.text == "بف":
       await message.reply_text(f"اجي وياكم 🌚💁") 
   elif message.text == "سلام عليكم":
       await message.reply_text(f"وعليكم السلام❤️") 
   








