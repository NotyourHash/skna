from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from HarshuXD import app 

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 



@app.on_message(
    filters.command("love", "I")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("❤️")
    await asyncio.sleep(0.5)
    await accha.edit("🧡")
    await asyncio.sleep(0.5)
    await accha.edit("💚")
    await asyncio.sleep(0.5)
    await accha.edit("💟")
    await asyncio.sleep(0.5)
    await accha.edit("💙")
    await asyncio.sleep(0.5)
    await accha.edit("💜")
    await asyncio.sleep(0.5)
    await accha.edit("🖤")
    await asyncio.sleep(0.5)
    await accha.edit("😻")
    await asyncio.sleep(0.5)
    await accha.edit("😍")
    await asyncio.sleep(0.5)
    await accha.edit("🤩")
    await asyncio.sleep(0.5)
    await accha.edit("😘")
    await asyncio.sleep(0.5)
    await accha.edit("😉")
    await asyncio.sleep(0.5)
    await accha.edit("🥰")
    await asyncio.sleep(0.5)
    await accha.edit("💘")
    await asyncio.sleep(0.5)
    await accha.edit("💝")
    await asyncio.sleep(0.5)
    await accha.edit("💖")
    await asyncio.sleep(0.5)
    await accha.edit("💗")
    await asyncio.sleep(0.5)
    await accha.edit("💓")
    await asyncio.sleep(0.5)
    await accha.edit("💞")
    await asyncio.sleep(0.5)
    await accha.edit("❣️")
    await asyncio.sleep(0.5)
    await accha.edit("ɪ")
    await asyncio.sleep(0.3)
    await accha.edit("ʟᴏᴠᴇ....🙈")
    await asyncio.sleep(0.3)
    await accha.edit("ʏᴏᴜ..🙊🙈")
    await asyncio.sleep(0.3)
    await accha.edit("ɪ ʟᴏᴠᴇ ʏᴏᴜ......💫💞")
    await asyncio.sleep(2.9)
    umm = await m.reply_sticker(

"CAACAgUAAxkBAAEHoY5l__0djAYm3aV-OOMv3YRhmH_t1AACNhMAAs8OAAFUohIjFXU5gFU0BA")
    await umm.delete()
    
    
