from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=22221341,
    api_hash="d4d93411808d4d8c0494a3b30293fb35",
    bot_token="7425080038:AAF1nEgPJq39yUeICySir7T6FM_UqeodCfg",
    plugins=dict(root="MZombie")
    )

DEVS = ["p_m_4","Maker_Marvenbot","G_O_OZ"] 

bot_id = bot.bot_token.split(":")[0]

async def start_Maker_Marvenbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
