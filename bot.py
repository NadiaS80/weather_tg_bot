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
    Handle the /start command. Sends a welcome message and displays the custom keyboard.

    Args:
        message (telebot.types.Message): Incoming Telegram message object.
    """
    bot.send_message(message.chat.id, "Привет 🌤️\nЯ бот прогноза погоды! Хочешь узнать погоду?", reply_markup=menu)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Handle all incoming text messages. If the user selects 'Погода на сегодня',
    asks for the city name and registers the next step handler.

    Args:
        message (telebot.types.Message): Incoming Telegram message object.
    """
    if message.text == 'Погода на сегодня':
        bot.send_message(message.chat.id, 'Напиши название города, погоду в котором хочешь узнать 🌍')
        bot.register_next_step_handler(message, get_weather)

def get_weather(message):
    """
    Fetch the weather forecast for the specified city and send it to the user.
    Handles any exceptions that occur during the process.

    Args:
        message (telebot.types.Message): Incoming Telegram message object.
    """
    try:
        city = message.text
        w = Weather(city)
        weather = w.weather_today()
        bot.send_message(message.chat.id, weather)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка 😕: {e}")


while True:
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Ошибка polling: {e}. Перезапуск через 5 секунд...")
        time.sleep(5)
