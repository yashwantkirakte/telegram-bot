from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def reply_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if text in ["hi", "hello"]:
        await update.message.reply_text("""👋 Welcome to Stoic Ops!
Your gateway to smart, strategic marketing discussions.
We’re the official Telegram companion for Stoic Ops, a thriving Reddit community where marketers, entrepreneurs, and creators come together
""")

app = ApplicationBuilder().token("7952724991:AAF0RIQ8sTCNoxS0p1CZlPcvEDlvTswkv4U").build()

app.add_handler(MessageHandler(filters.TEXT, reply_hi))

app.run_polling()