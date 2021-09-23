from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"🥴 Hello there, I am a telegram video streaming bot.\n\n💭 I was created to stream videos in group video chats easily.\n\n❔.To find out how to use me, please press the help button below 👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "Add Me", url="https://t.me/ghh?startgroup=true")
                       ],[
                          InlineKeyboardButton(
                             "😈 ᴢᴀɪᴅ ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀᴛ", url="https://t.me/zaid_team1")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/Itsunknown-12/Zaid-Video-Player")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/Zaid_Support"),
                          InlineKeyboardButton(
                             "🎑 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟꜱ", url="https://t.me/Zaid_Updates")
                       ]]
                    ))
   else:
      await m.reply("**✨ BOT IS ONLINE... ✨**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Zaid_Updates")
                       ],[
                          InlineKeyboardButton(
                             "🔥 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/Itsunknown-12/Zaid-Video-Player")
                       ],[
                          InlineKeyboardButton(
                             "📚 ʜᴇʟᴘ ᴀɴᴅ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/Zaid_Support")
                       ]]
                    )
                    )

