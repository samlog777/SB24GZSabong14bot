import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Read token from Railway environment variables
TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("No TELEGRAM_TOKEN found in environment variables.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I am SB24GZSabong14bot.\n"
        f"Use /help to see what I can do."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/ping - Check bot status\n"
        "/about - About this bot"
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check if the bot is alive."""
    await update.message.reply_text("Pong! I am alive.")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show about info."""
    await update.message.reply_text(
        "SB24GZSabong14bot\n"
        "A simple tool bot deployed on Railway.\n"
        "No external APIs used."
    )


def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("about", about))

    logging.info("Starting SB24GZSabong14bot with long polling...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
