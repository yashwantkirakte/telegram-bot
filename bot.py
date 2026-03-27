from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace this with your bot token
TOKEN = "YOUR_BOT_TOKEN_HERE"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! I'm your first Telegram bot.\nGlad to have you here!"
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
