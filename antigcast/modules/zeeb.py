from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from antigcast import Bot

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Start Zeeb
@Client.on_message(filter("start"))
async def start(Bot: Client, msg: Message):
    user = await Bot.get_me()
    mention = user.mention
    await Bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )


# Help Zeeb
@Client.on_message(filter("help"))
async def _help(Bot: Client, msg: Message):
    await Bot.send_message(
        msg.chat.id, Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# About dante
@Client.on_message(filter("about"))
async def about(Bot: Client, msg: Message):
    await Bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
  )
