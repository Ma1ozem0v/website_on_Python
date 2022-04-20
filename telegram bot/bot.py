# Импортируем необходимые классы.
# -*- coding: utf-8 -*-
import logging
import os
from random import randint

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import time

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


def start(update, context):
    reply_keyboard = [['/physics Физика', '/maths Математика', '/help Помощь']]
    markup = ReplyKeyboardMarkup(reply_keyboard,
                                 one_time_keyboard=False,
                                 resize_keyboard=True)
    text = 'Привет! Я бот-помощник в учебе. Нажмите на предмет и выберите нужный раздел.'
    update.message.reply_text(text, reply_markup=markup)


def close_keyboard(update, context):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def help(update, context):
    update.message.reply_text('Я бот, который может помочь Вам быстро найти информацию по школьным предметам.'
                              'Вы можете управлять мной через эти команды:'
                              '/start - начать использование бота'
                              ' /close - закрытие клавиатуры'
                              ' /back - кнопка назад'
                              ' /help - инструкцию по использованию бота'
                              ' /physics - раздел физики (другие функции содержатся в разделе)'
                              ' /maths - раздел математики (другие функции содержатся в разделе)'
                              ' В будущем функционал бота будет увеличен.')


def maths(update, context):
    reply_keyboard = [['/mfive 5-ый класс', '/msix 6-ой класс', '/mseven 7-ой класс'],['/meight 8-ой класс',
                       '/mnine 9-ый класс',  '/mten 10-ый класс'],
                      ['/meleven 11-ый класс', '/trigonometria синусы/косинусы/тангенсы/котангенсы', '/back назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard,
                                 one_time_keyboard=False,
                                 resize_keyboard=True)
    text = 'Формулы в математике'
    update.message.reply_text(text, reply_markup=markup)


def physics(update, context):
    reply_keyboard = [['/fseven 7-ой класс', '/feight 8-ой класс'], ['/fnine 9-ый класс',
                       '/ften 10-ый класс'], ['/feleven 11-ый класс', '/back назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard,
                                 one_time_keyboard=False,
                                 resize_keyboard=True)
    text = 'Формулы в физике'
    update.message.reply_text(text, reply_markup=markup)


def trigonometria(update, context):
    update.message.reply_text('Таблица синусов/косинусов/тангенсов/котангенсов.'
                              'Введите через / параметр: {sin,cos,tg,ctg}{угол} .'
                              ' Примеры: /sin60, /cos270, /tg30, /ctg45 и т.д.')


def mfive(update, context):
    text = f'Натуральные числа. Числа 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 и т. д., которые используют при счете предметов, называют натуральными. Сравнение натуральных чисе. Число 0 меньше любого натурального числа. Из двух натуральных чисел, которые имеют разное количество цифр большим является то, у которого количество цифр больше. Из двух натуральных чисел с одинаковым количеством цифр большим является то, у которого больше первая (при чтении слева направо) из неодинаковых цифр'
    update.message.reply_text(text)


def msix(update, context):
    text = f'Умножить число m на натуральное число n - значит найти сумму n слагаемых, каждое из которых равно m. Выражение m · n и значение этого выражения называют, произведением чисел m и n. Числа m и n называют множителями. Свойства умножения: 1. Переместительное свойство умножения: Произведение двух чисел не изменяется при перестановке множителей: a · b = b · а 2. Сочетательное свойство умножения: Чтобы умножить число на произведение двух чисел, можно сначала умножить его на первый множитель, а потом полученное произведение умножить на второй множитель: a · (b · с) = (а · b) · c. 3. Свойство умножения на единицу: Сумма n слагаемых, каждое из которых равно 1, равна n: 1 · n = n. 4. Свойство умножения на ноль: Сумма n слагаемых, каждое из которых равно нулю, равна нулю: 0 · n = 0. Знак умножения можно опускать: 8 · х = 8х, или а · b = ab, или a · (b + с) = a(b + с)'
    update.message.reply_text(text)


def mseven(update, context):
    text = f'Признаки делимости на 10 , на 5 и на 2. Если запись натурального числа оканчивается цифрой 0, то это число делится без остатка на 10. Если запись натурального числа оканчивается другой цифрой , то оно не делится без остатка на 10. Если запись натурального числа оканчивается цифрой 0 или 5 , то это число делится без остатка на 5. Если запись натурального числа оканчивается другой цифрой , то оно не делится без остатка на 5. Если запись натурального числа оканчивается четной цифрой , то это число делится без остатка на 2. Если запись натурального числа оканчивается нечетной цифрой , то это число нечетно.'
    update.message.reply_text(text)


def meight(update, context):
    text = 'Одночлены. Одночленами называют произведения чисел, переменных и их степеней, а также сами числа, переменные и их степени. Например, 8а3b,   –1,5xy2z8,   12,   с,   m10 — одночлены. Степенью одночлена называется сумма показателей степеней всех входящих в него переменных. Например, степень одночлена 9а7b равна 8. 4. Многочленом называется сумма одночленов. Например, у4 – 8у3 + 2у – 3,   4а4b + 11а2b2 – ab + 3b – 1 — многочлены. Одночлены считают многочленами, состоящими из одного члена. Степенью многочлена стандартного вида называют наибольшую из степеней входящих в него одночленов. Например, степень многочлена 18а6 – 7а4b3 + 1 равна степени одночлена –7а4b3, т. е. равна 7. Степенью произвольного многочлена называют степень тождественно равного ему многочлена стандартного вида.'
    update.message.reply_text(text)


def mnine(update, context):
    text = 'Арифметическая прогрессия. Арифметическая прогрессия – частный случай числовой последовательности.Например: Последовательность 2, 5, 8, 11, 14, ... является арифметической прогрессией с разностью d = 3. Последовательность 12, 9, 6, 3, 0, –3, –6, ... является арифметической прогрессией с разностью d = –3.'
    update.message.reply_text(text)


def mten(update, context):
    text = 'Определение производной. Пусть функция y=f(x) определена на некотором интервале, содержащим внутри себя некоторую точку x0. Приращение аргумента Δx – не выходит из нашего интервала. Найдем приращение Δy и составим отношение Δy/Δx, если существует предел этого отношения при Δx стремящимся к нулю, то указанный предел называют производной функции y=f(x) в точке x0 и обозначают f’(x0)'
    update.message.reply_text(text)


def meleven(update, context):
    text = f'Интеграл. Интеграл математическим языком – это первообразная функции (то, что было до производной) + константа «C». Интеграл простыми словами – это площадь криволинейной фигуры. Неопределенный интеграл – вся площадь. Определенный интеграл – площадь в заданном участке.'
    update.message.reply_text(text)


def fseven(update, context):
    text = f'Физика - наука, изучающая явления природы, свойства и строение материи. Явления – изменения, происходящие с телами и веществами в окружающем мире. Физические явления – любые превращения'
    update.message.reply_text(text)


def feight(update, context):
    text = 'Тепловое движение - беспорядочное движение частиц, из которых состоят тела, называют тепловым движением.  Внутренняя энергия тела - кинетическая энергия молекул, из которых состоит тело, и потенциальная энергия их взаимодействия составляют внутреннюю энергию тела'
    update.message.reply_text(text)


def fnine(update, context):
    text = 'Материальная точка - тело, размерами которого в условиях рассматриваемой задачи можно пренебречь. Поступательное движение - перемещение, в котором в любой момент все точки движутся одинаково.'
    update.message.reply_text(text)


def ften(update, context):
    text = 'Механика - раздел физики, в котором изучают закономерности механического движения тел и причины, вызывающие или изменяющие это движение. Кинематика - раздел механики, в котором изучают, как движется тело, без выяснения причин, вызвавших это движение. Тело отсчёта - тело, относительно которого рассматривают положение других тел'
    update.message.reply_text(text)


def feleven(update, context):
    text = 'Адроны - участвуют во всех четырёх взаимодействиях. Аккомодация - процесс при котором с помощью специальной мышцы хрусталик меняет свою кривизну - становится более или менее выпуклым и соответственно сильнее или слабее преломляет попадающие в глаз лучи света. Активное сопротивление - сопротивление электрической цепи или её участка, обуславливающее превращение электрической энергии в другие виды энергии.'
    update.message.reply_text(text)


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


def tg0(update, context):
    update.message.reply_text('0')


def tg30(update, context):
    update.message.reply_text('1/√3')


def tg45(update, context):
    update.message.reply_text('1')


def tg60(update, context):
    update.message.reply_text('√3')


def tg90(update, context):
    update.message.reply_text('-')


def tg120(update, context):
    update.message.reply_text('-√3')


def tg135(update, context):
    update.message.reply_text('-1')


def tg150(update, context):
    update.message.reply_text('-1/√3')


def tg180(update, context):
    update.message.reply_text('0')


def tg270(update, context):
    update.message.reply_text('-')


def tg360(update, context):
    update.message.reply_text('0')


def ctg0(update, context):
    update.message.reply_text('-')


def ctg30(update, context):
    update.message.reply_text('√3')


def ctg45(update, context):
    update.message.reply_text('1')


def ctg60(update, context):
    update.message.reply_text('1/√3')


def ctg90(update, context):
    update.message.reply_text('0')


def ctg120(update, context):
    update.message.reply_text('-1/√3')


def ctg135(update, context):
    update.message.reply_text('-1')


def ctg150(update, context):
    update.message.reply_text('-√3')


def ctg180(update, context):
    update.message.reply_text('-')


def ctg270(update, context):
    update.message.reply_text('0')


def ctg360(update, context):
    update.message.reply_text('-')


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('back', start))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('maths', maths))
    dp.add_handler(CommandHandler('physics', physics))
    dp.add_handler(CommandHandler('feleven', feleven))
    dp.add_handler(CommandHandler('meleven', meleven))
    dp.add_handler(CommandHandler('fseven', fseven))
    dp.add_handler(CommandHandler('feight', feight))
    dp.add_handler(CommandHandler('fnine', fnine))
    dp.add_handler(CommandHandler("ften", ften))
    dp.add_handler(CommandHandler("mfive", mfive))
    dp.add_handler(CommandHandler('msix', msix))
    dp.add_handler(CommandHandler('mseven', mseven))
    dp.add_handler(CommandHandler('meight', meight))
    dp.add_handler(CommandHandler('mnine', mnine))
    dp.add_handler(CommandHandler('mten', mten))
    dp.add_handler(CommandHandler("trigonometria", trigonometria))
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
    dp.add_handler(CommandHandler("tg0", tg0))
    dp.add_handler(CommandHandler("tg30", tg30))
    dp.add_handler(CommandHandler("tg45", tg45))
    dp.add_handler(CommandHandler("tg60", tg60))
    dp.add_handler(CommandHandler("tg90", tg90))
    dp.add_handler(CommandHandler("tg120", tg120))
    dp.add_handler(CommandHandler("tg135", tg135))
    dp.add_handler(CommandHandler("tg150", tg150))
    dp.add_handler(CommandHandler("tg180", tg180))
    dp.add_handler(CommandHandler("tg270", tg270))
    dp.add_handler(CommandHandler("tg360", tg360))
    dp.add_handler(CommandHandler("ctg0", ctg0))
    dp.add_handler(CommandHandler("ctg30", ctg30))
    dp.add_handler(CommandHandler("ctg45", ctg45))
    dp.add_handler(CommandHandler("ctg60", ctg60))
    dp.add_handler(CommandHandler("ctg90", ctg90))
    dp.add_handler(CommandHandler("ctg120", ctg120))
    dp.add_handler(CommandHandler("ctg135", ctg135))
    dp.add_handler(CommandHandler("ctg150", ctg150))
    dp.add_handler(CommandHandler("ctg180", ctg180))
    dp.add_handler(CommandHandler("ctg270", ctg270))
    dp.add_handler(CommandHandler("ctg360", ctg360))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
