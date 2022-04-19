import logging
import os
from dotenv import load_dotenv
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот-помощник в учебе. Нажмите на предмет и выберите нужный раздел.", reply_markup=markup)


def close_keyboard(update, context):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def help(update, context):
    update.message.reply_text('Я бот, который может помочь Вам быстро найти информацию по школьным предметам.'
                              'Вы можете управлять мной через эти команды:'
                              '/start - начать использование бота'
                              '/close - закрытие клавиатуры'
                              '/help - инструкцию по использованию бота'
                              '/physics - раздел физики'
                              '/maths - раздел математики'
                              'В будущем функционал бота будет увеличен.')


reply_keyboard = [['/help', '/physics', '/maths']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("help", help))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()