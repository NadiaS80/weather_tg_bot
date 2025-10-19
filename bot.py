import telebot
from telebot import types
from weather_cod import Weather
import time


BOT_TOKEN = 'YOUR-KEY'

bot = telebot.TeleBot(BOT_TOKEN)


menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
weather_today = types.KeyboardButton('Погода на сегодня')
menu.add(weather_today)

@bot.message_handler(commands=['start'])
def start_message(message):
    """
    Handles the /start command sent by the user.

    Sends a welcome message and displays a custom keyboard with weather options.

    Args:
        message (telebot.types.Message): Incoming Telegram message object containing
                                         chat and user information.
    """
    bot.send_message(message.chat.id, "Привет 🌤️\nЯ бот прогноза погоды! Хочешь узнать погоду?", reply_markup=menu)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Handles all text messages sent to the bot.

    Detects whether the user requested today's or tomorrow's forecast and
    forwards control to the appropriate weather handler.

    Args:
        message (telebot.types.Message): Incoming Telegram message object.
    """
    if message.text == 'Погода на сегодня':
        bot.send_message(message.chat.id, 'Напиши название города, погоду в котором хочешь узнать 🌍')
        bot.register_next_step_handler(message, today_get_weather)
    elif message.text == 'Погода на завтра':
        bot.send_message(message.chat.id, 'Напиши название города, погоду в котором хочешь узнать 🌍')
        bot.register_next_step_handler(message, tomorrow_get_weather)


def today_get_weather(message):
    """
    Processes the user's input city and sends the weather forecast for today.

    Args:
        message (telebot.types.Message): Telegram message containing the city name.
    """
    try:
        city = message.text
        w = Weather(city)
        weather = w.weather_today()
        bot.send_message(message.chat.id, weather)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка 😕: {e}")

def tomorrow_get_weather(message):
    """
    Processes the user's input city and sends the weather forecast for tomorrow.

    Args:
        message (telebot.types.Message): Telegram message containing the city name.
    """
    try:
        city = message.text
        w = Weather(city)
        weather = w.weather_tommorow()
        bot.send_message(message.chat.id, weather)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка 😕: {e}")


while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Ошибка polling: {e}. Перезапуск через 5 секунд...")
        time.sleep(5)

