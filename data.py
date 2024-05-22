from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Add me your group", url="https://t.me/AntiBroadcastPyro_Bot?startgroup=true")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Channel", url="https://t.me/RuangZeeb")],
        [
            InlineKeyboardButton("Command", callback_data="help"),
            InlineKeyboardButton("Support", callback_data="about")
        ],
        [InlineKeyboardButton("Owner", url="https://t.me/Zeebdisini")],
    ]

    START = """
Hey {}

Saya adalah {}
Bot ini bisa melakuka hapus pesan spam secara otomatis yang mengganggu digrup anda

 """

    HELP = """
**Perintah yang Tersedia**
/antigcast on/off = Mengaktifkan dan menonaktifkan
/remove = Menambahkan pesan dalam database blacklist
/delmsg = Menghapus blacklist kata dalam database
/adduser = Menambahkan pengguna kedalam database antigcast
/deluser = Menghapus pengguna dalam database antigcast
/getuser = Melihat daftar pengguna yang terblacklist
"""

    ABOUT = """
**Tentang Bot Ini** 
bots that can delete or help you with group trash problems.

bot ini bisa digunakan disemua group.

jika ada masalah pada bot silahkan hubungi:
@zeebdisini || @ZeebSupport
    """
