import telebot
from telebot import types
import math
import statistics
from math import factorial as fact
try:  # SciPy >= 0.19
    from scipy.special import comb, logsumexp
except ImportError:
    from scipy.misc import comb, logsumexp  # noqa 


TOKEN = '6174907011:AAGLox1HBdSH1WE_1pPR2HdLYtMZqGBR_jI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    # Создаем кнопки
    buttons = [
        types.KeyboardButton("Умножение на константу"),
        types.KeyboardButton("Определитель"),
        types.KeyboardButton("Медиана"),
        types.KeyboardButton("Среднее геометрическое"),
        types.KeyboardButton("Среднее гармоническое"),
        types.KeyboardButton("Среднее квадратическое"),
        types.KeyboardButton("Натуральный логарифм"),
        types.KeyboardButton("Десятичный логарифм"),
        types.KeyboardButton("Логарифм"),
        types.KeyboardButton("Среднее логарифмическое"),
        types.KeyboardButton("НОК"),
        types.KeyboardButton("НОД"),
        types.KeyboardButton("Факториал"),
        types.KeyboardButton("Количество сочетаний"),
        types.KeyboardButton("Субфакториал"),
        types.KeyboardButton("Среднее арифметическое"),
        types.KeyboardButton("Корень степени n"),
        types.KeyboardButton("Знак числа"),
        types.KeyboardButton("Проверка на простоту"),
        types.KeyboardButton("Решение линейного уравнения"),
        types.KeyboardButton("Гиперфакториал")
    ]
    
    # Добавляем кнопки в клавиатуру
    markup.add(*buttons)
    
    # Приветственное сообщение
    bot.send_message(message.chat.id, "Привет! Я бот для вычисления математических действий. Выберите действие:", reply_markup=markup)

# Функция для обработки выбора кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Умножение на константу":
        bot.send_message(message.chat.id, "Введите число для умножения:")
        bot.register_next_step_handler(message, multiply_constant)
    elif message.text == "Определитель":
        bot.send_message(message.chat.id, "Введите матрицу в формате 'a b; c d' для 2x2:")
        bot.register_next_step_handler(message, determinant)
    elif message.text == "Медиана":
        bot.send_message(message.chat.id, "Введите числа через пробел для нахождения медианы:")
        bot.register_next_step_handler(message, median)
    elif message.text == "Среднее геометрическое":
        bot.send_message(message.chat.id, "Введите числа через пробел для нахождения среднего геометрического:")
        bot.register_next_step_handler(message, geometric_mean)
    elif message.text == "Среднее гармоническое":
        bot.send_message(message.chat.id, "Введите числа через пробел для нахождения среднего гармонического:")
        bot.register_next_step_handler(message, harmonic_mean)
    elif message.text == "Среднее квадратическое":
        bot.send_message(message.chat.id, "Введите числа через пробел для нахождения среднего квадратического:")
        bot.register_next_step_handler(message, quadratic_mean)
    elif message.text == "Натуральный логарифм":
        bot.send_message(message.chat.id, "Введите число для вычисления натурального логарифма:")
        bot.register_next_step_handler(message, natural_log)
    elif message.text == "Десятичный логарифм":
        bot.send_message(message.chat.id, "Введите число для вычисления десятичного логарифма:")
        bot.register_next_step_handler(message, decimal_log)
    elif message.text == "Логарифм":
        bot.send_message(message.chat.id, "Введите число и основание логарифма через пробел:")
        bot.register_next_step_handler(message, logarithm)
    elif message.text == "Среднее логарифмическое":
        bot.send_message(message.chat.id, "Введите числа через пробел для нахождения среднего логарифмического:")
        bot.register_next_step_handler(message, logarithmic_mean)
    elif message.text == "НОК":
        bot.send_message(message.chat.id, "Введите два числа для нахождения НОК через пробел:")
        bot.register_next_step_handler(message, lcm)
    elif message.text == "НОД":
        bot.send_message(message.chat.id, "Введите два числа для нахождения НОД через пробел:")
        bot.register_next_step_handler(message, gcd)
    elif message.text == "Факториал":
        bot.send_message(message.chat.id, "Введите число для вычисления факториала:")
        bot.register_next_step_handler(message, factorial)
    elif message.text == "Количество сочетаний":
        bot.send_message(message.chat.id, "Введите n и k через пробел для вычисления сочетаний:")
        bot.register_next_step_handler(message, combinations)
    elif message.text == "Субфакториал":
        bot.send_message(message.chat.id, "Введите число для вычисления субфакториала:")
        bot.register_next_step_handler(message, subfactorial)
    elif message.text == "Среднее арифметическое":
        bot.send_message(message.chat.id, "Введите числа через пробел для нахождения среднего арифметического:")
        bot.register_next_step_handler(message, arithmetic_mean)
    elif message.text == "Корень степени n":
        bot.send_message(message.chat.id, "Введите число и степень корня через пробел:")
        bot.register_next_step_handler(message, nth_root)
    elif message.text == "Знак числа":
        bot.send_message(message.chat.id, "Введите число для определения знака:")
        bot.register_next_step_handler(message, sign_of_number)
    elif message.text == "Проверка на простоту":
        bot.send_message(message.chat.id, "Введите число для проверки на простоту:")
        bot.register_next_step_handler(message, prime_check)
    elif message.text == "Решение линейного уравнения":
        bot.send_message(message.chat.id, "Введите коэффициенты a и b через пробел для уравнения ax+b=0:")
        bot.register_next_step_handler(message, solve_linear_equation)
    elif message.text == "Гиперфакториал":
        bot.send_message(message.chat.id, "Введите число для вычисления гиперфакториала:")
        bot.register_next_step_handler(message, hyperfactorial)

# Функции-обработчики для каждой математической операции
def multiply_constant(message):
    try:
        number = float(message.text)
        result = number * 2  # Замена 2 на любую константу
        bot.send_message(message.chat.id, f"Результат: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите число.")

def determinant(message):
    try:
        rows = message.text.split(';')
        matrix = [list(map(float, row.split())) for row in rows]
        if len(matrix) == 2 and all(len(row) == 2 for row in matrix):
            result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            bot.send_message(message.chat.id, f"Определитель: {result}")
        else:
            bot.send_message(message.chat.id, "Ошибка: введите матрицу 2x2.")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа корректно.")

def median(message):
    try:
        numbers = list(map(float, message.text.split()))
        result = statistics.median(numbers)
        bot.send_message(message.chat.id, f"Медиана: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа через пробел.")

def geometric_mean(message):
    try:
        numbers = list(map(float, message.text.split()))
        result = statistics.geometric_mean(numbers)
        bot.send_message(message.chat.id, f"Среднее геометрическое: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа через пробел.")

def harmonic_mean(message):
    try:
        numbers = list(map(float, message.text.split()))
        result = statistics.harmonic_mean(numbers)
        bot.send_message(message.chat.id, f"Среднее гармоническое: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа через пробел.")

def quadratic_mean(message):
    try:
        numbers = list(map(float, message.text.split()))
        result = math.sqrt(sum(x**2 for x in numbers) / len(numbers))
        bot.send_message(message.chat.id, f"Среднее квадратическое: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа через пробел.")

def natural_log(message):
    try:
        number = float(message.text)
        result = math.log(number)
        bot.send_message(message.chat.id, f"Натуральный логарифм: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите положительное число.")

def decimal_log(message):
    try:
        number = float(message.text)
        result = math.log10(number)
        bot.send_message(message.chat.id, f"Десятичный логарифм: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите положительное число.")

def logarithm(message):
    try:
        base, number = map(float, message.text.split())
        result = math.log(number, base)
        bot.send_message(message.chat.id, f"Логарифм: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите основание и число через пробел.")

def logarithmic_mean(message):
    try:
        numbers = list(map(float, message.text.split()))
        if all(x > 0 for x in numbers):
            result = sum(math.log(x) for x in numbers) / len(numbers)
            bot.send_message(message.chat.id, f"Среднее логарифмическое: {math.exp(result)}")
        else:
            bot.send_message(message.chat.id, "Ошибка: все числа должны быть положительными.")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа через пробел.")

def lcm(message):
    try:
        a, b = map(int, message.text.split())
        result = abs(a * b) // math.gcd(a, b)
        bot.send_message(message.chat.id, f"НОК: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите два целых числа через пробел.")

def gcd(message):
    try:
        a, b = map(int, message.text.split())
        result = math.gcd(a, b)
        bot.send_message(message.chat.id, f"НОД: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите два целых числа через пробел.")

def factorial(message):
    try:
        n = int(message.text)
        result = math.factorial(n)
        bot.send_message(message.chat.id, f"Факториал: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите неотрицательное целое число.")

def combinations(message):
    try:
        n, k = map(int, message.text.split())
        result = comb(n, k)
        bot.send_message(message.chat.id, f"Количество сочетаний: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите два целых числа через пробел.")

def subfactorial(message):
    try:
        n = int(message.text)
        result = round(math.factorial(n) / math.e)
        bot.send_message(message.chat.id, f"Субфакториал: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите неотрицательное целое число.")

def arithmetic_mean(message):
    try:
        numbers = list(map(float, message.text.split()))
        result = sum(numbers) / len(numbers)
        bot.send_message(message.chat.id, f"Среднее арифметическое: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите числа через пробел.")

def nth_root(message):
    try:
        number, degree = map(float, message.text.split())
        result = number ** (1 / degree)
        bot.send_message(message.chat.id, f"Корень {degree}-ой степени: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите число и степень через пробел.")

def sign_of_number(message):
    try:
        number = float(message.text)
        result = "Положительное" if number > 0 else "Отрицательное" if number < 0 else "Ноль"
        bot.send_message(message.chat.id, f"Знак числа: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите число.")

def prime_check(message):
    try:
        n = int(message.text)
        if n < 2:
            result = "Число не является простым."
        else:
            result = "Число является простым." if all(n % i != 0 for i in range(2, int(n**0.5) + 1)) else "Число не является простым."
        bot.send_message(message.chat.id, result)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите целое число.")

def solve_linear_equation(message):
    try:
        a, b = map(float, message.text.split())
        if a != 0:
            result = -b / a
            bot.send_message(message.chat.id, f"Решение уравнения: x = {result}")
        else:
            bot.send_message(message.chat.id, "Ошибка: коэффициент 'a' не должен быть равен 0.")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите два числа через пробел.")

def hyperfactorial(message):
    try:
        n = int(message.text)
        result = 1
        for i in range(1, n + 1):
            result *= i**i
        bot.send_message(message.chat.id, f"Гиперфакториал: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: введите неотрицательное целое число.")

# Запуск бота

bot.polling()