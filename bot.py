from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="6405234806:AAEKv4P8kbUkcYMDTQv7r2RvSPv9p4zAhRw",
    plugins=dict(root="MZombie")
    )

DEVS = ["p_m_4","Zo_Mbi_e","G_O_OZ"] 

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
