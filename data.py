from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Tambahkan ke grup", url="https://t.me/AntiBroadcastPyro_Bot?startgroup=true")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Kembali", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Chanel", url="https://t.me/ZeebSupport")],
        [
            InlineKeyboardButton("Perintah", callback_data="help"),
            InlineKeyboardButton("Bantuan", callback_data="about")
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
