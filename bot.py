from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Get token from environment variable
TOKEN = os.getenv("TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Create buttons
    keyboard = [
        [InlineKeyboardButton("🌐 Website", url="https://stoic-ops.com/")],
        [InlineKeyboardButton("📢 Telegram", url="https://t.me/stoicops")],
        [InlineKeyboardButton("💬 Discord", url="https://discord.com/invite/au7BbcANKE")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with buttons
    await update.message.reply_text(
        """👋 Welcome to Stoic Ops!
Your gateway to smart, strategic marketing discussions.

We’re the official Telegram companion for Stoic Ops, a thriving Reddit community where marketers, entrepreneurs, and creators come together. \n join us on following platforms.""",
        reply_markup=reply_markup
    )

# Main function
def main():
    if not TOKEN:
        raise ValueError("TOKEN is not set! Please set environment variable.")

    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()