
import requests
import datetime
from transformers import MarianMTModel, MarianTokenizer
import emoji


class Translate:
    """
    Class for translating text between Russian and English using MarianMT models.

    Attributes:
        text (str): The text to be translated.
    """

    def __init__(self, text):
        """
        Initialize a Translate object.

        Args:
            text (str): Text to be translated.
        """
        self.text = text

    @staticmethod
    def _load_model(src_lang, tgt_lang):
        """
        Load a MarianMT tokenizer and model for the specified language pair.

        Args:
            src_lang (str): Source language code ('ru' or 'en').
            tgt_lang (str): Target language code ('ru' or 'en').

        Returns:
            tuple: (tokenizer, model) for translation.
        """
        name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        tok = MarianTokenizer.from_pretrained(name)
        model = MarianMTModel.from_pretrained(name)
        return tok, model

    @staticmethod
    def _translate(text, tokenizer, model):
        """
        Translate text using the provided MarianMT tokenizer and model.

        Args:
            text (str): Text to translate.
            tokenizer: MarianMT tokenizer.
            model: MarianMT model.

        Returns:
            str: Translated text.
        """
        batch = tokenizer([text], return_tensors="pt", truncation=True, padding=True)
        gen = model.generate(**batch)
        return tokenizer.decode(gen[0], skip_special_tokens=True)


    def translate_word_ru_en(self):
        """
        Translate text from Russian to English.

        Returns:
            str: Translated text in English.
        """
        tok_ru_en, model_ru_en = self._load_model('ru', 'en')
        src = self.text
        return self._translate(src, tok_ru_en, model_ru_en)


    def translate_word_en_ru(self):
        """
        Translate text from English to Russian.

        Returns:
            str: Translated text in Russian.
        """
        tok_en_ru, model_en_ru = self._load_model('en', 'ru')
        src = self.text
        return self._translate(src, tok_en_ru, model_en_ru)



class Weather:
    """
    Class for fetching weather forecast using the Visual Crossing API.

    Attributes:
        API_key (str): API key for accessing Visual Crossing.
        url_weather (str): URL for weather forecast requests.
        location (str): City name in English.
    """

    API_key = 'YOUR-KEY'
    url_weather = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

    def __init__(self, location):
        """
        Initialize a Weather object.

        Args:
            location (str): City name in Russian.
        """
        translate = Translate(location)
        self.location = translate.translate_word_ru_en()

    def weather_today(self, date=None):
        """
        Get the weather forecast for a specific date, or today if no date is provided.

        Args:
            date (datetime.date, optional): Date for the forecast. Defaults to today.

        Returns:
            str: Formatted weather forecast including temperature, precipitation, wind, cloudiness, visibility,
                 sunrise/sunset, and textual description.
        """
        if date is None:
            date = datetime.date.today() 
        date1 = date
        params = {'location': self.location,
          'key': self.API_key,
          'date1': date1,
          'unitGroup': 'base'
          }
        response = requests.get(self.url_weather, params=params)
        json_weather = response.json()
        temp_med = json_weather['days'][0]['temp'] - 273.15
        temp_max = json_weather['days'][0]['tempmax'] - 273.15
        temp_min = json_weather['days'][0]['tempmin'] - 273.15
        feel_temp_med = json_weather['days'][0]['feelslike'] - 273.15
        feel_temp_max = json_weather['days'][0]['feelslikemax'] - 273.15
        feel_temp_min = json_weather['days'][0]['feelslikemin'] - 273.15
        humidity = json_weather['days'][0]['humidity'] # air humidity as a percentage
        precip = json_weather['days'][0]['precip'] # the amount of precipitation in millimeters
        precipprob = json_weather['days'][0]['precipprob'] # percentage probability of precipitation %
        preciptype = json_weather['days'][0]['preciptype'] # rain/snow/mixed precipitation, precipitation type (if not, returns None)
        if preciptype is None:
            preciptype = 'Нет'
        elif isinstance(preciptype, list):
            for info in preciptype:
                preciptype = ', '.join([Translate(info).translate_word_en_ru() for info in preciptype])
        else:
            preciptype = Translate(preciptype).translate_word_en_ru()
        windspeed = json_weather['days'][0]['windspeed']
        windgust = json_weather['days'][0]['windgust'] # wind gusts, maximum speed (meters per second)
        winddir = json_weather['days'][0]['winddir'] # wind direction in degrees, where 0 is north
        cloudcover = json_weather['days'][0]['cloudcover'] # percentage of the sky covered with clouds
        visibility = json_weather['days'][0]['visibility'] # Visibility: Kilometers, the distance at which objects can be seen
        sunrise = json_weather['days'][0]['sunrise'] # sunrise time
        sunset = json_weather['days'][0]['sunset'] # sunset time
        uvindex = json_weather['days'][0]['uvindex'] # the level of ultraviolet radiation
        conditions = json_weather['days'][0]['conditions'] # a brief description of the weather conditions
        translate = Translate(conditions)
        conditions = translate.translate_word_en_ru()
        description = json_weather['days'][0]['description'] # detailed description of the weather
        translate = Translate(description)
        description = translate.translate_word_en_ru()
        weather_forecast = (
            f"\n🌍 Прогноз погоды на {str(date.strftime('%d.%m.%Y')).replace('-', '.')}:\n\n"
            f"{emoji.emojize(':thermometer:')} Температура:\n"
            f"  • Минимальная — {temp_min:.0f}°C (ощущается {feel_temp_min:.0f}°C)\n"
            f"  • Средняя — {temp_med:.0f}°C (ощущается {feel_temp_med:.0f}°C)\n"
            f"  • Максимальная — {temp_max:.0f}°C (ощущается {feel_temp_max:.0f}°C)\n\n"
            f"{emoji.emojize(':umbrella_with_rain_drops:')} Осадки:\n"
            f"  • Тип — {preciptype}\n"
            f"  • Вероятность — {precipprob}%\n"
            f"  • Количество — {precip} мм\n\n"
            f"{emoji.emojize(':wind_face:')} Ветер:\n"
            f"  • Скорость — {windspeed} м/с\n"
            f"  • Порывы — {windgust} м/с\n"
            f"  • Направление — {winddir}°\n\n"
            f"{emoji.emojize(':cloud:')} Облачность:\n"
            f"  • Облачность — {cloudcover}%\n"
            f"  • Видимость — {visibility} км\n\n"
            f"{emoji.emojize(':sunrise:')} Солнце:\n"
            f"  • Восход — {sunrise[:5]}\n"
            f"  • Закат — {sunset[:5]}\n"
            f"  • УФ-индекс — {uvindex}\n\n"
            f"{emoji.emojize(':microphone:')} О погоде:\n"
            f"  - {conditions}\n"
            f"  - {description}\n"
        )
        return weather_forecast