import asyncio

from antigcast import Bot
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, MessageDeleteForbidden, UserNotParticipant

from antigcast.config import *
from antigcast.helpers.tools import *
from antigcast.helpers.admins import *
from antigcast.helpers.message import *
from antigcast.helpers.database import *


@Bot.on_message(filters.command("remove") & ~filters.private & Admin)
async def addblmessag(app : Bot, message : Message):
    trigger = get_arg(message)
    if message.reply_to_message:
        trigger = message.reply_to_message.text or message.reply_to_message.caption

    xxnx = await message.reply(f"`Message` {trigger} `added to blacklist`")
    try:
        await add_bl_word(trigger.lower())
    except BaseException as e:
        return await xxnx.edit(f"Error : `{e}`")

    try:
        await xxnx.edit(f"{trigger} `Successfully added to the list`")
    except:
        await app.send_message(message.chat.id, f"{trigger} `Successfully added to the list`")

    await asyncio.sleep(5)
    await xxnx.delete()
    await message.delete()

@Bot.on_message(filters.command("delmsg") & ~filters.private & Admin)
async def deldblmessag(app : Bot, message : Message):
    trigger = get_arg(message)
    if message.reply_to_message:
        trigger = message.reply_to_message.text or message.reply_to_message.caption

    xxnx = await message.reply(f"`Delete` {trigger} `the list`")
    try:
        await remove_bl_word(trigger.lower())
    except BaseException as e:
        return await xxnx.edit(f"Error : `{e}`")

    try:
        await xxnx.edit(f"{trigger} `Successfully removed from the list`")
    except:
        await app.send_message(message.chat.id, f"{trigger} `Successfully removed from the list`")

    await asyncio.sleep(5)
    await xxnx.delete()
    await message.delete()


@Bot.on_message(filters.text & ~filters.private & Member & Gcast)
async def deletermessag(app : Bot, message : Message):
    text = f"***Sorry, the group is not registered, contact @zeebdisini to register your group**"
    chat = message.chat.id
    chats = await get_actived_chats()
    if chat not in chats:
        await message.reply(text=text)
        await asyncio.sleep(5)            
    # Delete
    try:
        await message.delete()
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await message.delete()
    except MessageDeleteForbidden:
        pass
