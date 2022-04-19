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


def maths(update, context):
    update.message.reply_text('На данный момент в разделе математики доступно: '
                              'таблица синусов/косинусов/тангенсов/котангенсов.'
                              'Введите через / параметр: {sin,cos,tg,ctg}{угол} .'
                              ' Примеры: /sin60, /tg30 и т.д.')


def sin0(update, context):
    update.message.reply_text('0')


def sin30(update, context):
    update.message.reply_text('1/2')


def sin45(update, context):
    update.message.reply_text('√2/2')


def sin60(update, context):
    update.message.reply_text('√3/2')


def sin90(update, context):
    update.message.reply_text('1')


def sin120(update, context):
    update.message.reply_text('√3/2')


def sin135(update, context):
    update.message.reply_text('√2/2')


def sin150(update, context):
    update.message.reply_text('1/2')


def sin180(update, context):
    update.message.reply_text('0')


def sin270(update, context):
    update.message.reply_text('-1')


def sin360(update, context):
    update.message.reply_text('0')


def cos0(update, context):
    update.message.reply_text('1')


def cos30(update, context):
    update.message.reply_text('√3/2')


def cos45(update, context):
    update.message.reply_text('√2/2')


def cos60(update, context):
    update.message.reply_text('1/2')


def cos90(update, context):
    update.message.reply_text('0')


def cos120(update, context):
    update.message.reply_text('-1/2')


def cos135(update, context):
    update.message.reply_text('-√2/2')


def cos150(update, context):
    update.message.reply_text('-√3/2')


def cos180(update, context):
    update.message.reply_text('-1')


def cos270(update, context):
    update.message.reply_text('0')


def cos360(update, context):
    update.message.reply_text('1')


reply_keyboard = [['/help', '/physics', '/maths']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("maths", maths))
    dp.add_handler(CommandHandler("sin0", sin0))
    dp.add_handler(CommandHandler("sin30", sin30))
    dp.add_handler(CommandHandler("sin45", sin45))
    dp.add_handler(CommandHandler("sin60", sin60))
    dp.add_handler(CommandHandler("sin90", sin90))
    dp.add_handler(CommandHandler("sin120", sin120))
    dp.add_handler(CommandHandler("sin135", sin135))
    dp.add_handler(CommandHandler("sin150", sin150))
    dp.add_handler(CommandHandler("sin180", sin180))
    dp.add_handler(CommandHandler("sin270", sin270))
    dp.add_handler(CommandHandler("sin360", sin360))
    dp.add_handler(CommandHandler("cos0", cos0))
    dp.add_handler(CommandHandler("cos30", cos30))
    dp.add_handler(CommandHandler("cos45", cos45))
    dp.add_handler(CommandHandler("cos60", cos60))
    dp.add_handler(CommandHandler("cos90", cos90))
    dp.add_handler(CommandHandler("cos120", cos120))
    dp.add_handler(CommandHandler("cos135", cos135))
    dp.add_handler(CommandHandler("cos150", cos150))
    dp.add_handler(CommandHandler("cos180", cos180))
    dp.add_handler(CommandHandler("cos270", cos270))
    dp.add_handler(CommandHandler("cos360", cos360))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()