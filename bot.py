from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import os
import asyncio

# Get token from Railway environment variable
TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN VALUE:", TOKEN)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Welcome! 👋")

async def reply_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        
        if text in ["hi", "hello"]:
            await update.message.reply_text("Welcome! 👋")

# Create app
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply_hi))

# Run bot
asyncio.run(app.run_polling())
