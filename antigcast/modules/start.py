import asyncio

from antigcast import Bot
from pyrogram import filters, enums
from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from antigcast.config import *
from antigcast.helpers.database import *
import traceback
from data import Data

CTYPE = enums.ChatType

#callback -_-

@Client.on_callback_query()
async def _callbacks(Bot: Client, callback_query: CallbackQuery):
    user = await Bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await Bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )

# callback2
@Bot.on_callback_query(filters.regex(r"close"))
async def close_cbq(client: Bot, query: CallbackQuery):
    try:
        await query.message.reply_to_message.delete()
        await client.send_message(query.from_user.id, "**Pendaftaran Dibatalkan**")
    except:
        pass
    try:
        await query.message.delete()
        await client.send_message(query.from_user.id, "**Pendaftaran Dibatalkan**")
    except:
        pass

@Bot.on_callback_query(filters.regex(r"langganan"))
async def bayar_cbq(client: Bot, query: CallbackQuery):
    btn = InlineKeyboardMarkup(admin_panel())
    text = """**Silahkan pilih Plan Subscription untuk berlangganan Bot Anti Gcast**

1 Bulan : `Rp. 25.000,-`
3 Bulan : `RP. 60.000,-`"""
    await query.edit_message_text(
        text = text,
        reply_markup = btn
    )
