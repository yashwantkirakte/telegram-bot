from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os


# Replace this with your bot token
TOKEN = os.getenv("TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """👋 Welcome to Stoic Ops!
Your gateway to smart, strategic marketing discussions.
We’re the official Telegram companion for Stoic Ops, a thriving Reddit community where marketers, entrepreneurs, and creators come together"""
    )

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
