
import requests
import datetime
from transformers import MarianMTModel, MarianTokenizer
import emoji
from AI_hf import AI_HF


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

    API_KEY = "YOUR-KEY"
    url_weather = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'


    def __init__(self, location):
        """
        Initializes a Weather instance with a translated location name.

        Args:
            location (str): The original city or location name provided by the user.
                            It will be translated via the AI_HF class to match
                            the format expected by the weather API.
        """
        translate_ai = AI_HF(location)
        self.location = translate_ai.translate()


    def _day_get_weather(self, date):
        """
        Retrieves detailed weather information for a specific date and location.

        Args:
            date (datetime.date): The date for which the weather data should be retrieved.

        Returns:
            str: A formatted string containing temperature, wind, precipitation,
                 humidity, visibility, and other weather details for the given day.
        """
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
        humidity = json_weather['days'][0]['humidity'] # влажность воздуха в процентах
        precip = json_weather['days'][0]['precip'] # количество выпавших осадков в миллиметрах
        precipprob = json_weather['days'][0]['precipprob'] # вероятность осадков в процентах %
        preciptype = json_weather['days'][0]['preciptype'] # дождь/снег/смешанные осадки, тип осадков (если нет, то возвращает None)
        if preciptype is None:
            preciptype = 'Нет'
        elif isinstance(preciptype, list):
            for info in preciptype:
                preciptype = ', '.join([Translate(info).translate_word_en_ru() for info in preciptype])
        else:
            preciptype = Translate(preciptype).translate_word_en_ru()
        windspeed = json_weather['days'][0]['windspeed']
        windgust = json_weather['days'][0]['windgust'] # порывы ветра, максимальная скорость (метров в секунду)
        winddir = json_weather['days'][0]['winddir'] # направление ветра в градусах, где 0 — север
        cloudcover = json_weather['days'][0]['cloudcover'] # процент неба, покрытого облаками 
        visibility = json_weather['days'][0]['visibility'] # Видимость: Километры, расстояние, на котором можно разглядеть объекты
        sunrise = json_weather['days'][0]['sunrise'] # время восхода солнца
        sunset = json_weather['days'][0]['sunset'] # время захода солнца
        uvindex = json_weather['days'][0]['uvindex'] # уровень ультрафиолетового излучения
        conditions = json_weather['days'][0]['conditions'] # краткое описание погодных условий
        description = json_weather['days'][0]['description'] # подробное описание погоды
        base_forecast = (
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
        )
        info_forecast = base_forecast + (f"{conditions}, {description}")
        ai = AI_HF(info_forecast)
        ai_forecast = ai.formating_answer(self.location, date1)
        weather_forecast = base_forecast + ai_forecast
        return weather_forecast


    def weather_today(self, date=None):
        """
        Gets the weather forecast for the current day.

        Args:
            date (datetime.date, optional): A specific date for the forecast. Defaults to today.

        Returns:
            str: A formatted weather report for the current day.
        """
        if date is None:
            date = datetime.date.today()
        weather_forecast = self._day_get_weather(date)
        return weather_forecast


    def weather_tommorow(self, date=None):
        """
        Gets the weather forecast for the next day.

        Args:
            date (datetime.date, optional): A specific date for the forecast. Defaults to tomorrow.

        Returns:
            str: A formatted weather report for the next day.
        """
        if date is None:
            today = datetime.date.today() 
            date = datetime.timedelta(1) + today
        weather_forecast = self._day_get_weather(date)
        return weather_forecast