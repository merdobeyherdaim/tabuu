import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# Bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Game state variables
game_state = {}
players = []

# Start command
def start(update: Update, context):
    update.message.reply_text('Vampir oyununa hoş geldiniz! /help komutunu kullanarak bilgi alabilirsiniz.')

# Help command
def help_command(update: Update, context):
    update.message.reply_text("Oyun komutları:\n/start - Oyuna başla\n/help - Yardım al")

# Game Start Command
def game_start(update: Update, context):
    keyboard = [[InlineKeyboardButton("Başla", callback_data='start_game')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Oyunu başlatmak için aşağıdaki butona tıklayın:", reply_markup=reply_markup)

# Button callback handling
def button(update: Update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'start_game':
        query.edit_message_text(text="Oyuna başlıyoruz! Takımlar belirlenecek...")
        # Game start logic here

# Main function to run the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("game", game_start))

    # Button handler
    dp.add_handler(CallbackQueryHandler(button))

    # Start polling
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()

if __name__ == '__main__':
    main()
