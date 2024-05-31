import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AdRenalen import app
import random
    

@app.on_message(command([f"صوره", "صورة", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )



@app.on_message(command([f"استوريهات", "استوري", "استيت"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/yoipopl{rl}"
    await client.send_photo(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )


@app.on_message(command(["صوره انمي", "انمي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
    
                                                              
@app.on_message(command(["استيكر", "متحركه"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
    

    
    
@app.on_message(command(["صور بنات", "افاتار بنات"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
    
                            
@app.on_message(command(["صور شباب", "افاتار شباب"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
    

@app.on_message(command(["سوره", "قرآن"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/opuml/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
                       
@app.on_message(command(["الشيخ", "النقشبندي", "نقشبندي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_audio(message.chat.id,url,caption="- Join.Channel.SouRce : @SOURCE_MARVEN ⋅",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )

