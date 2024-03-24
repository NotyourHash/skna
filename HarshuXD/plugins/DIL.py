from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from HarshuXD import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

DIL = [" **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**ɪ ᴀᴍ sᴜᴋᴜɴᴀ, ᴛʜᴇ ᴋɪɴɢ ᴏғ ᴄᴜʀsᴇs**🍃 \n\n** ᴛʜᴇ ᴇᴍʙᴏᴅɪᴍᴇɴᴛ ᴏғ ᴘᴏᴡᴇʀ ᴀɴᴅ ᴍᴀʟɪᴄᴇ ** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** ",
       " **◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** \n\n🍃**🌹❝◂ ᴛʜᴀᴛ ʜᴀs ᴇᴄʜᴏᴇᴅ  ▸**🍃 \n\n** ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴀɴɴᴀʟs ᴏғ ᴛɪᴍᴇ** \n\n**◈ ━━━━━━━ ⸙ ♡ ⸙ ━━━━━━━ ◈** "]

# Command of DILxAAROHI
DIL_COMMAND = get_command("DIL_COMMAND")

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴩᴩᴏʀᴛ[ʜᴇʟʟ]", url=f"https://t.me/EquinoxBots"),
                    InlineKeyboardButton(
                        "ᴍᴀɪɴᴛᴀɪɴᴇʀ[ʟᴏʀᴅ]", url=f"https://t.me/Harshu_Huu")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DIL_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(DIL),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜᴩᴩᴏʀᴛ[ʜᴇʟʟ]", url=f"https://t.me/EquinoxBots"),
                    InlineKeyboardButton(
                        "ᴍᴀɪɴᴛᴀɪɴᴇʀ[ʟᴏʀᴅ]", url=f"https://t.me/Harshu_Huu")
                    
                ]
            ]
        ),
    )
