# DipeshxD - MissKristinaBot
# Copyright (C) 2021 TeamUltroid
# This file is a part of < https://github.com/DipeshxD/MissKristinaBot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/DipeshxD/MissKristinaBot/blob/main/LICENSE/>.


import os
from MashaRoBot import pbot as Lovely
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def get_channel_id_from_input(bot, message):
    try:
        a_id = message.text.split(" ", 1)[1]
    except:
        await message.reply_text("**Send cmd along with channel id**")
        return False
    if not str(a_id).startswith("-"):
        try:
            a_id = await bot.get_chat(a_id)
            a_id = a_id.id
        except:
            await message.reply_text("**Inavalid channel id**")
            return False
    return a_id

@Lovely.on_message(filters.command(["chban"]) & filters.group)
async def cban_handler(bot, message):
    chat_id = message.chat.id
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status == "creator" or user.status == "administrator":
        pass
    else:
        return
    try:
        a_id = await get_channel_id_from_input(bot, message)
        await bot.resolve_peer(a_id)
        res = await bot.kick_chat_member(chat_id, a_id)
        chat_data = await bot.get_chat(a_id)
        mention = f"@{chat_data.username}" if chat_data.username else chat_data.title
        if res:
            await message.reply_text(
                text=f"**Banned channel {mention} from group.**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "Unban", callback_data=f"unban_{chat_id}_{a_id}"
                            )
                        ]
                    ]
                ),
            )
        else:
            await message.reply_text("**Invalid Channel id**")
    except Exception as e:
        print(e)

@Lovely.on_message(filters.command(["chunban"]) & filters.group)
async def uncban_handler(bot, message):
    chat_id = message.chat.id
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status == "creator" or user.status == "administrator":
        pass
    else:
        return
    try:
        a_id = await get_channel_id_from_input(bot, message)
        if not a_id:
            return
        await bot.resolve_peer(a_id)
        res = await message.chat.unban_member(a_id)
        chat_data = await bot.get_chat(a_id)
        mention = f"@{chat_data.username}" if chat_data.username else chat_data.title
        if res:
            await message.reply_text(
                text=f"**{mention} has been unbanned by {message.from_user.mention}**"
            )
        else:
            await message.reply_text("**Invalid Channel id**")
    except Exception as e:
        print(e)
        await message.reply_text(e)

@Lovely.on_callback_query()
async def cb_handler(bot, query):
    cb_data = query.data
    if cb_data.startswith("unban_"):
        an_id = cb_data.split("_")[-1]
        chat_id = cb_data.split("_")[-2]
        user = await bot.get_chat_member(chat_id, query.from_user.id)
        if user.status == "creator" or user.status == "administrator":
            pass
        else:
            return await query.answer("This Message is Not For You!", show_alert=True)
        await bot.resolve_peer(an_id)
        res = await query.message.chat.unban_member(an_id)
        chat_data = await bot.get_chat(an_id)
        mention = f"@{chat_data.username}" if chat_data.username else chat_data.title
        if res:
            await query.message.edit_text(
                f"**{mention} has been unbanned by {query.from_user.mention}**"
            )
            await query.message.edit_reply_markup(reply_markup=None)
__help__ = """
You can ban those users who are chatting using channel
Ban channel
Command `/chban <channel id>`
Unban channel
Command `/chunban <channel id`
"""

__mod_name__ = "Cʜᴀɴɴᴇʟʙᴀɴ🚫"
