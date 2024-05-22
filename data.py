from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Add Me To Group", url="https://t.me/AntiBroadcastPyro_Bot?startgroup=true")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Bot other", url="https://t.me/MusicStreamMp3/5")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Developer", url="https://t.me/Usern4meDoesNotExist404")],
    ]

    START = """
Hey {}

Welcome to {}
Bot ini akan menghapus otomatis pesan gcast yang mengganggu 
di group. Tambahkan bot sebagai admin agar bisa membantu kamu
 
 """

    HELP = """
**Perintah yang Tersedia**
/on & /off = untuk mematikan dan menghidupkan anti gcast (only admin)
/groups = untuk melihat daftar gtoup yang menggunakan antigcast.
/cekuser = untuk melihat daftar pengguna yang di balcklist.
/adduser = untuk menambah pengguna ke dalam database antigcast
/remuser = untuk menghapus pengguna di dalam database antigcast
/cek = untuk mengecek apakah antigcast telah di aktifkan
/addgc = untuk menambah grup sebagai antigcast
/rmgc = untuk menghapus group agar tidak bisa menggunakan antigcast
/add = tambahkan group ke dalam anti gcast
/bl = untuk menambah pesan antigcast
/tagall = untuk mention/tagall anggota didalam group
/cancel = untuk memberhentikan mention/tagall di dalam group
/unbl = untuk menghapus kata yang di blacklist
"""

    ABOUT = """
**Tentang Bot Ini** 
bots that can delete or help you with group trash problems.

bot ini bisa digunakan disemua group.

jika ada masalah pada bot silahkan hubungi:
@Usern4meDoesNotExist404 || @StreamSupportMp3
    """
