# plugins/key.py

async def handle_app_paid(bot, data, call_msg, a):
    await call_msg.edit_text("✅ App marked as paid!\n\n📦 Data:\n" + str(data))
