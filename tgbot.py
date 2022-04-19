# Импортируем необходимые классы.
# -*- coding: utf-8 -*-
import logging
import os
from random import randint

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
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
    reply_keyboard = [['/physics Физика', '/maths Математика']]
    markup = ReplyKeyboardMarkup(reply_keyboard,
                                 one_time_keyboard=False,
                                 resize_keyboard=True)
    text = 'Бот-помощник для физики и математики'
    update.message.reply_text(text, reply_markup=markup)


def maths(update, context):
    reply_keyboard = [['/mfive 5-ый класс', '/msix 6-ой класс', '/mseven 7-ой класс', '/meight 8-ой класс',
                       '/mnine 9-ый класс',  '/mten 10-ый класс', '/meleven 11-ый класс']]
    markup = ReplyKeyboardMarkup(reply_keyboard,
                                 one_time_keyboard=False,
                                 resize_keyboard=True)
    text = 'Формулы в математике'
    update.message.reply_text(text, reply_markup=markup)


def physics(update, context):
    reply_keyboard = [['/fseven 7-ой класс', '/feight 8-ой класс', '/fnine 9-ый класс',
                       '/ften 10-ый класс', '/feleven 11-ый класс', '/back назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard,
                                 one_time_keyboard=False,
                                 resize_keyboard=True)
    text = 'Формулы в физике'
    update.message.reply_text(text, reply_markup=markup)


def mfive(update, context):
    text = f'Натуральные числа. Числа 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 и т. д., которые используют при счете предметов, называют натуральными. Сравнение натуральных чисе. Число 0 меньше любого натурального числа. Из двух натуральных чисел, которые имеют разное количество цифр большим является то, у которого количество цифр больше. Из двух натуральных чисел с одинаковым количеством цифр большим является то, у которого больше первая (при чтении слева направо) из неодинаковых цифр'
    update.message.reply_text(text)


def msix(update, context):
    text = f'Умножить число m на натуральное число n - значит найти сумму n', f'слагаемых, каждое из которых равно m.', f'Выражение m · n и значение этого выражения называют', f'произведением чисел m и n. Числа m и n называют множителями.', f'Свойства умножения:', f'1. Переместительное свойство умножения: Произведение двух чисел не изменяется', f'при перестановке множителей: a · b = b · а', f'2. Сочетательное свойство умножения: Чтобы умножить число на произведение двух', f'чисел, можно сначала умножить его на первый множитель, а потом полученное', f'произведение умножить на второй множитель: a · (b · с) = (а · b) · c.', f'3. Свойство умножения на единицу: Сумма n слагаемых, каждое из которых равно 1,', f'равна n: 1 · n = n.', f'4. Свойство умножения на ноль: Сумма n слагаемых, каждое из которых равно нулю,', f'равна нулю: 0 · n = 0.', f'Знак умножения можно опускать: 8 · х = 8х, или а · b = ab, или a · (b + с) = a(b + с)'
    update.message.reply_text(text)


def mseven(update, context):
    text = f'Признаки делимости на 10 , на 5 и на 2. Если запись натурального числа оканчивается цифрой 0 , то это число делится без остатка на 10. Если запись натурального числа оканчивается другой цифрой , то оно не делится без остатка на 10. Если запись натурального числа оканчивается цифрой 0 или 5 , то это число делится без остатка на 5. Если запись натурального числа оканчивается другой цифрой , то оно не делится без остатка на 5. Если запись натурального числа оканчивается четной цифрой , то это число делится без остатка на 2. Если запись натурального числа оканчивается нечетной цифрой , то это число нечетно.'
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


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('back', start))
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

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
