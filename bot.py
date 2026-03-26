from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import asyncio

# 👉 Paste your bot token here (from BotFather)
TOKEN = os.getenv("7952724991:AAF0RIQ8sTCNoxS0p1CZlPcvEDlvTswkv4U")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("""👋 Welcome to Stoic Ops!
Your gateway to smart, strategic marketing discussions.
We’re the official Telegram companion for Stoic Ops, a thriving Reddit community where marketers, entrepreneurs, and creators come together""")

async def reply_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        
        if text in ["hi", "hello"]:
            await update.message.reply_text("""👋 Welcome to Stoic Ops!
Your gateway to smart, strategic marketing discussions.
We’re the official Telegram companion for Stoic Ops, a thriving Reddit community where marketers, entrepreneurs, and creators come together""")

# Create app
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply_hi))

# Run bot
asyncio.run(app.run_polling())
