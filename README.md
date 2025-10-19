# 🌤 WeatherBot – Telegram Weather Forecast Bot

Welcome to **WeatherBot**! A cozy Telegram bot that gives **detailed, human-friendly weather forecasts** for any city 🌍.  
It supports Russian city names, fixes typos, detects the correct country, fetches weather data from Visual Crossing, and adds **fun, engaging commentary** via HuggingFace AI 😎

---

## ⚡ Features

- 🌡 **Temperature** – min, max, average, feels like  
- ☔ **Precipitation** – type, probability, amount  
- 🌬 **Wind** – speed, gusts, direction  
- ☁ **Cloudiness & Visibility**  
- 🌅 **Sunrise & Sunset** times  
- 🌞 **UV Index**  
- 📝 **Weather commentary** – HuggingFace AI converts raw data into short, human-readable summaries with humor and emojis  
- 🌐 **Smart city input handling** – supports Russian and fuzzy city names, automatically translates, corrects spelling, detects country, and ensures accurate API requests  
- 📅 **Tomorrow’s forecast support** – added new method `weather_tommorow()` and Telegram button *"Погода на завтра"* for next-day predictions  

---

## 📂 File Structure

```text
WeatherBot/
│
├─ bot.py             # Telegram bot interface 💬
├─ weather_cod.py     # Weather class: fetches, formats, and sends weather data 🌍
├─ AI_hf.py           # HuggingFace AI integration for human-friendly commentary 🤖
├─ requirements.txt   # Python dependencies 📦
└─ README.md          # Project overview 📖
```

---

## 🛠 Installation & Setup

1. **Clone this repository:**
```bash
git clone https://github.com/NadiaS80/weather_tg_bot.git
```

2. **Navigate to the project folder:**
```bash
cd WeatherBot
```

3. **Install dependencies (Python 3.10+ required):**
```bash
pip install -r requirements.txt
```

---

## 🛠 Setup API Tokens

- **Telegram bot token** → replace `YOUR-KEY` in `bot.py`  
- **Visual Crossing API key** → replace `YOUR-KEY` in `weather_cod.py`  
- **HuggingFace API token** → replace `YOUR-KEY` in `AI_hf.py`

> 🔒 **Security:** Never share your API keys publicly. Keep your token files safe.

---

## 📝 Usage

1. **Run the bot:**
```bash
python bot.py
```

2. **Open Telegram** → start your bot → type `/start`  
   Then choose:
   - **"Погода на сегодня"** → get today’s forecast  
   - **"Погода на завтра"** → get tomorrow’s forecast  

3. **Enter a city name (in any language)** — the bot automatically translates it and fetches data.

4. **Receive a detailed weather forecast with:**
   - Automatic city correction & country detection  
   - Human-style commentary from HuggingFace AI  
   - Emoji-enhanced, natural weather summaries 🌈  

**📦 Sample output:**
```
🌍 Прогноз погоды на 08.10.2025:

🌡️ Температура:
  • Минимальная — 19°C (ощущается 19°C)
  • Средняя — 20°C (ощущается 20°C)
  • Максимальная — 22°C (ощущается 22°C)

☔️ Осадки:
  • Тип — дождь
  • Вероятность — 100.0%
  • Количество — 13.0 мм

🌬️ Ветер:
  • Скорость — 6.6 м/с
  • Порывы — 9.4 м/с
  • Направление — 178.2°

☁️ Облачность:
  • Облачность — 100.0%
  • Видимость — 6.9 км

🌅 Солнце:
  • Восход — 05:26
  • Закат — 17:54
  • УФ-индекс — 1.0

🎤 О погоде:
Сегодня в Рио-де-Жанейро небо решило устроить настоящий водный марафон — дождь идёт без передышки, но хотя бы тёплый, почти как в парке Тихука после тропического ливня 🌧️🥵. Температура держится на комфортных 20°C, так что можно смело брать зонт и наслаждаться свежестью — тем более, что к вечеру закат всё равно прорвётся сквозь тучи 🌇. Только ветер, похоже, тренируется для карнавала — порывы до 9 м/с! 💨
```

---

## 📦 Dependencies

- `requests` – fetch API data  
- `telebot` (`pyTelegramBotAPI`) – Telegram bot interface  
- `transformers` – MarianMT translation models  
- `emoji` – emoji rendering  
- `datetime` – date and time management (for `weather_today()` and `weather_tommorow()`)

---

## 🚀 Roadmap / Future Plans

- 🌡 **Real-Time Weather** – instant weather for any city worldwide  
- 🌅 **Tomorrow’s Forecast** – already implemented via `weather_tommorow()` 🎉  
- 📆 **Multi-Day Forecasts** – 3-day & weekly summaries  
- ⏰ **Scheduled Notifications** – daily weather alerts at user-defined times  
- 🌐 **Geolocation Detection** – auto-detect user location for instant forecasts  
- 🗣️ **Language Options** – Russian & English support  
- 🌠 **Extended Integrations** – NASA APIs & visual weather cards  

💡 **Goal:** Make WeatherBot smarter, faster, and more personal 🌈✨

---

## 🤝 Contributing

- Fork, improve, or customize your version  
- Pull requests and feature suggestions are welcome 🚀  

---

## 🎉 Enjoy!

Get forecasts **anytime, anywhere**, with HuggingFace-powered commentary and emoji charm 🌤️💬
