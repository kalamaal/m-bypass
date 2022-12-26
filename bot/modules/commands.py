import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import exceptions, UserNotParticipant
from bot import CMD
from bot.welpers.translations import lang
from bot.welpers.utilities import bypasser
from bot.modules.database.access_db import db
from bot.modules.database.database import Database
from bot.modules.important import humanbytes, TimeFormatter, broadcast_handler

LOG_CHANNEL = os.environ.get("LOG_CHANNEL", '-1001742793568')
BOT_OWNER = os.environ.get("BOT_OWNER", '5468863203')

start_keyboard = [
    [
        InlineKeyboardButton("♻️ Update Channel", url="https://t.me/DKBOTZ"),
        InlineKeyboardButton("Tutorial Video", url="https://t.me/DK_BOTZ")
    ],
    [
        InlineKeyboardButton('❌ Close', callback_data = "close")
    ]
]

about_keyboard = InlineKeyboardMarkup([
     [
        InlineKeyboardButton('🤔 How To Download Video', url="https://t.me/DKBOTZ")
    ],
    [
        InlineKeyboardButton("♻️ Update Channel", url="https://t.me/DK_BOTZ")
    ]
])

@Client.on_message(filters.command(CMD.START))
async def start(bot, update):
    reply_markup = InlineKeyboardMarkup(start_keyboard)
    await update.reply_text(
        text=lang.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup = reply_markup,
        quote=True,
    )

@Client.on_message(filters.command(CMD.MDIK) & filters.regex(r"https?://[^\s]+"))
async def mdik(bot, update):

    url = update.matches[0].group(0)
    ouo = bypasser.mdisk(url)
    await asyncio.sleep(2)
    messagez = await update.reply_text(
        text=ouo, disable_web_page_preview=True, quote=True)
    await asyncio.sleep(2)
    forward_ = await messagez.forward(chat_id=LOG_CHANNEL)
    await forward_.reply_text(
        text=f"**User:** [{update.from_user.first_name}](tg://user?id={str(update.from_user.id)})\n**Username:** `{update.from_user.username}`\n**UserID:** `{update.from_user.id}`",
        disable_web_page_preview=True,
        quote=True
     )
@Client.on_message(filters.command("broadcast") & filters.reply & filters.user(BOT_OWNER))
async def broadcast(bot, update):
    await broadcast_handler(bot, update)


@Client.on_message(filters.command("status") & filters.user(BOT_OWNER))
async def status(bot, update):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await update.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )
