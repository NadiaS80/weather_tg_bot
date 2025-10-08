# 🌤 WeatherBot – Telegram Weather Forecast Bot

Welcome to **WeatherBot**! This is a simple, cozy Telegram bot that gives you weather forecasts for any city in Russia 🌍.  
It translates Russian city names to English, fetches data from Visual Crossing API, and gives you a beautiful weather summary with emojis 🌈.

---

## ⚡ Features

- 🌡 Shows **temperature** (min, max, average, feels like)  
- ☔ Displays **precipitation** info (type, probability, amount)  
- 🌬 Provides **wind data** (speed, gusts, direction)  
- ☁ Cloudiness & visibility  
- 🌅 Sunrise & sunset times  
- 🌞 UV index  
- 📝 Short and long **weather descriptions**  
- 🌐 Supports **Russian city names**, automatically translating them to English  

---

## 🛠 Installation

1. Clone this repository:  
   ```bash
   git clone <your-repo-url>
   ```

## 🛠 Installation

2. Navigate to the project folder:  
```bash
cd WeatherBot
```

## 🛠 Install Dependencies

Make sure you have **Python 3.10+** installed. Then install the required packages:  
```bash
pip install -r requirements.txt
```

## 📦 Dependencies Include

- `requests` – for fetching API data  
- `telebot` (pyTelegramBotAPI) – for Telegram bot interface  
- `transformers` – for MarianMT translation models  
- `emoji` – for displaying emojis  

---

## 🔑 Setup

1. Get a **Telegram bot token** from [BotFather](https://t.me/BotFather)  
2. Replace `'YOUR-KEY'` in `bot.py` with your token  
3. Get a **Visual Crossing API key** from [Visual Crossing](https://www.visualcrossing.com/)  
4. Replace `'YOUR-KEY'` in `weather_cod.py` with your API key  

---

## 📝 Usage

1. Run the bot:  
```bash
python bot.py
```

## 📝 Usage

1. Open Telegram and start your bot by typing `/start`  
2. Click **"Погода на сегодня"**  
3. Enter the **city name in Russian**  
4. Receive a **detailed weather forecast** with emojis 😎  

---

## 📂 File Structure

- `weather_cod.py` – Contains `Weather` and `Translate` classes for fetching and translating weather data 🌍  
- `bot.py` – Telegram bot interface, uses `Weather` class to send forecasts 💬  

---

## 🤝 Contributing

Feel free to **fork**, **improve**, or make your own version!  
Suggestions and PRs are welcome 🚀  

---

## ⚠ Notes

- The bot **needs an active internet connection**  
- Free MarianMT models are used, so the **first translation might take a few seconds**  
- Make sure your **API key for Visual Crossing** is valid 🗝️  

---

## 🚀 Future Plans / Roadmap

Our WeatherBot is evolving! Here's what you can expect in upcoming updates:  

### 🌡️ Real-Time Weather  
- Get instant weather for your current city or any city worldwide.  
- Perfect for checking conditions before heading out.  

### 🌅 Tomorrow’s Forecast  
- Receive detailed predictions for the next day.  
- Know in advance if you need an umbrella, jacket, or sunglasses.  

### 📆 Multi-Day Forecasts  
- 3-day and weekly weather summaries.  
- Plan your week ahead with confidence.  

### ⏰ Scheduled Notifications  
- Set personalized alerts to receive daily forecasts at a chosen time.  
- Example: get tomorrow’s weather every evening at 8 PM automatically.  

### 🌐 Optional Geolocation Integration (Future)  
- Auto-detect your location for instant forecasts.  
- Useful for on-the-go updates without typing the city name.  

### 🗣️ Language Options  
- English & Russian supported.  
- Easily switch languages for international users.  

### 🌠 Long-Term Integrations  
- API integrations with NASA or other weather-related services.  
- Add visual content like weather images, icons, or seasonal illustrations.  

💡 These features are designed to make WeatherBot smarter, faster, and more personal! Stay tuned for updates! 🌈✨


---

## 🎉 Enjoy!

Now you can have weather updates **anywhere, anytime**, with a touch of emoji magic 🌈✨
