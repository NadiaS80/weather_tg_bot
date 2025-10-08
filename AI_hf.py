import requests


class AI_HF:
    """
    AI_HF class for interacting with a HuggingFace-based AI model to:

    1. Translate city names from various languages (mostly Russian) into 
       standardized English format: "City, Country".
    2. Generate human-friendly, conversational weather commentary 
       based on structured weather data.

    Attributes:
        API_URL (str): HuggingFace API endpoint for chat completions.
        HUGGING_FACE_TOKEN (str): Bearer token for authenticating requests.
        text (str): Input text, either city name for translation or raw weather data for commentary.
    """
    API_URL = 'https://router.huggingface.co/v1/chat/completions'
    HUGGING_FACE_TOKEN = 'YOUR-KEY'

    def __init__(self, text):
        self.text = text


    def translate(self):
        """
        Translate a city name into standardized English format "City, Country".

        This method sends a request to the HuggingFace AI model, providing
        instructions to:
        - Correct spelling errors.
        - Handle small or obscure cities.
        - Always return properly capitalized city and country names.
        - Avoid adding extra text, symbols, or punctuation.

        Returns:
            str: Translated city in the format "City, Country".
        """
        headers = {'Authorization': f'Bearer {self.HUGGING_FACE_TOKEN}'}
        main_promt = f"""
Ты — умный и точный конвертер названий городов в корректный английский формат. 
Твоя задача — на основе полученного от пользователя названия города на любом языке, чаще всего на русском, определить город и страну и выдать результат в формате: City, Country

Учти:
- исправляй опечатки в названии города;
- работай с маленькими и малоизвестными городами;
- всегда используй правильное написание английских названий;
- не добавляй ничего лишнего: ни точек, ни скобок, ни подчеркиваний, ни вопросов, ни приветствий;
- всегда выводи через запятую и пробел, с большой буквы для города и страны;
- примеры: "Воронеж" → "Voronezh, Russia", "Поворино" → "Povorino, Russia", "Нью-Йорк" → "New York, USA".
"""

        negative_promt = f"""
Не делай следующее:
- не добавляй пояснения, подсказки, вопросы, приветствия;
- не используй лишние символы, точки, скобки, подчеркивания;
- не меняй порядок: всегда сначала город, затем страна;
- не используй нижний регистр или некорректный верхний регистр;
- не добавляй дополнительные слова или детали (например, область, регион, координаты);
- не пытайся красиво описывать город, только корректное название и страна.
"""
        payload = {
            'messages': [
                {
                    'role': 'user',
                    'content': (
                        f'Есть отправленный пользователем город {self.text}. '
                        f'Выполни задания, описанные дальше. Позитивный промт: {main_promt}. Негативный промт: {negative_promt}.'
                        f'Как уже было описано выше, твой ответ должен быть в формате: City, Country'
                    )
                }
            ],
            'model': 'deepseek-ai/DeepSeek-V3-0324'
        }

        response = requests.post(self.API_URL, headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']




    def formating_answer(self, location, date, now_date=datetime.date.today()):
        """
        Generate a human-readable, conversational weather commentary.

        This method sends structured weather data to the AI model, 
        instructing it to:
        - Analyze temperature, cloud cover, precipitation, wind, UV index, etc.
        - Add light humor, emotion, and a friendly tone.
        - Include local details if the city is known for something.
        - Insert relevant emojis (1–3), not overly childish.
        - Avoid AI disclaimers, repeated phrases, or formal language.

        Args:
            location (str): Standardized city name in the format "City, Country".
            date (datetime.date): The target date for the weather forecast.
            now_date (datetime.date, optional): The current date, defaults to today.

        Returns:
            str: Formatted weather forecast with human-friendly commentary, 
                 including metrics and emoji-enhanced description.
        """
        headers = {'Authorization': f'Bearer {self.HUGGING_FACE_TOKEN}'}

        main_promt = f"""
Ты — умный, человечный и дружелюбный комментатор погоды. 
Твоя задача — на основе полученных данных о погоде в городе написать короткий, разговорный комментарий от 2 до 5 предложений. 

Учти:
- анализируй всё: температуру, облачность, осадки, ветер, солнечный индекс, влажность, время года, время суток (если указано), местоположение;
- добавь лёгкий оптимизм, эмоции и живой тон — будто рассказываешь другу, но без обращения напрямую;
- если погода сложная — будь реалистичным, но подбодри («дождь не помешает прогулке ☔»);
- если город известен чем-то (например, красивыми осенними парками в Ванкувере или снежными зимами в Москве) — можно добавить локальную деталь;
- вставляй уместные эмодзи (1–3), не детские, не шаблонные, только если они усиливают смысл;
- можно лёгкий юмор («ветер сегодня явно решил стать тренером по кардио 💨»);
- можешь давать советы по погоде, если это логично («лучше взять зонт», «самое время для прогулки»).

Твоя цель — сделать погоду “человечной”: чтобы человек почувствовал атмосферу, настроение дня и лёгкое воодушевление. 
Не задавай встречных вопросов, не упоминай, что ты нейросеть или модель.
"""

        negative_promt = f"""
Не делай следующее:
- не задавай встречных вопросов;
- не используй фразы вроде "по данным модели", "как ИИ", "согласно прогнозу", "по нашим данным";
- не будь роботоподобным, не повторяй одни и те же слова;
- не используй избыточный пафос или чрезмерные восклицания;
- не используй детские, нелепые или неуместные смайлы;
- не начинай ответ с приветствия;
- не уходи в длинные научные объяснения — только эмоция, ощущение и смысл.
"""
        
        payload = {
            'messages': [
                {
                    'role': 'user',
                    'content': (
                        f'Есть данные о погоде в городе {location}. '
                        f'На {date} дату. Сегодня {now_date}. '
                        f'Данные: {self.text}. '
                        f'Проанализируй и напиши короткий комментарий в человеческом, живом, эмоциональном стиле — как описано в инструкциях дальше. '
                        f'Позитивный промт: {main_promt}. '
                        f'Негативный промт: {negative_promt}.'
                        f'Основной язык ответа - русский'
                    )
                }
            ],
            'model': 'deepseek-ai/DeepSeek-V3-0324'
        }

        response = requests.post(self.API_URL, headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
