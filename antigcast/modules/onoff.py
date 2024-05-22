import asyncio
import datetime

from pytz import timezone
from dateutil.relativedelta import relativedelta

from antigcast import Bot
from pyrogram import filters
from pyrogram.types import Message

from antigcast.config import *
from antigcast.helpers.tools import *
from antigcast.helpers.database import *
from antigcast.helpers.database import admin_filter


# BY DANTE 
@Bot.on_message(filters.command(["on"]) & admin_filter)
async def antigcaston(app : Bot, message : Message):
    chat_id = message.chat.id
    chat_name = message.chat.title
    hari = get_arg(message)
    if not hari:
        hari = "30"
    xxnx = await message.reply(f"`Anti gcast berhasil di aktifkan!`")
    now = datetime.datetime.now(timezone("Asia/Jakarta"))
    expired = now + relativedelta(days=int(hari))
    expired_date = expired.strftime("%d-%m-%Y")
    chats = await get_actived_chats()
    if chat_id in chats:
        msg = await message.reply("Silahkan hidupkan anti gcast /on agar bot bisa digunakan.")
        await asyncio.sleep(10)
        await msg.delete()
        return
    
    try:
        added = await add_actived_chat(chat_id)
        if added:
            await set_expired_date(chat_id, expired)
    except BaseException as e:
        print(e)

    await xxnx.edit(f"Anti broadcast on di group : `{chat_name}`")
    await asyncio.sleep(10)
    await xxnx.delete()
    await message.delete()

@Bot.on_message(filters.command(["off"]) & admin_filter)
async def antigcastoff(app : Bot, message : Message):
    chat_id = get_arg(message)

    if not chat_id:
        chat_id = message.chat.id
        
    xxnx = await message.reply(f"`Anti broadcast Berhasil di nonaktifkan`")
    try:
        await rem_actived_chat(chat_id)
        await rem_expired_date(chat_id)
    except BaseException as e:
        print(e)

    await xxnx.edit(f"Anti Gcast berhasil di nonaktifkan di `{chat_id}`, bot akan stop menghapus gcast!`")
    await asyncio.sleep(10)
    await xxnx.delete()
    await message.delete()
