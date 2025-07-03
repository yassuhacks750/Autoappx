from pyrogram import Client as bot, filters
from constant import buttom, msg
from config import Config
from master.utils import send_random_photo
import os, sys
##Code Written By @ItsMeMaster
@bot.on_message(filters.command("start") & filters.private)
async def start_msg(bot, m):
    user_mention = m.from_user.mention
    await bot.send_photo(m.chat.id,photo=await send_random_photo(),caption=msg.START.format(user_mention, Config.USERLINK), reply_markup=buttom.home())


@bot.on_message(filters.command("help") & filters.private)
async def help_msg(bot, m):
    await bot.send_photo(m.chat.id,photo=await send_random_photo(),caption=msg.HELP.format(Config.USERLINK), reply_markup=buttom.help_keyboard())

##Code Written By @ItsMeMaster

@bot.on_message(filters.command("restart") & filters.private)
async def restart_handler(_, m):
    if m.chat.id != Config.ADMIN_ID:
        return await m.reply_text(
            "╭━━━━━━ ERROR ━━━━━━➣\n"
            "┣⪼ ⚠️ **Access Denied**\n"
            "┣⪼ 🔒 Admin only command\n"
            "╰━━━━━━━━━━━━━━━━➣"
        )
    await m.reply_text("🚦**Restarting...**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command("legal") & filters.private)
async def legal_disclaimer(_, m):
    await m.reply_text(msg.DISCLAIMER,disable_web_page_preview=True,reply_markup=buttom.contact())

##Code Written By @ItsMeMaster

@bot.on_message(filters.command("id"))
async def get_chat_id(_, m):
    await m.reply_text(f"<blockquote><b>The ID of this chat id is:</b></blockquote> `{m.chat.id}`")
    
