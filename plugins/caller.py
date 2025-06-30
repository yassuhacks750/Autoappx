from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
import json
from plugins import key  # Make sure key.py exists in plugins

@Client.on_callback_query(filters.regex("^app_paid"))
async def app_paid_callback(bot: Client, callback_query: CallbackQuery):
    try:
        data = json.loads(callback_query.data.split("||")[1])
        call_msg = callback_query.message
        a = "some value"  # Replace with actual data if needed
        await key.handle_app_paid(bot, data, call_msg, a)
    except Exception as e:
        await callback_query.answer("Error occurred.", show_alert=True)
        print(e)
