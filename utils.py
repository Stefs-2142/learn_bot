from clarifai.rest import ClarifaiApp
import settings
from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def play_random_number(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!'
    elif user_number == bot_number:
        message = f'Ты загадал {user_number} и я тоже. Ничья!'
    else:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ты проиграл!'
    return message


def main_keyboard():
    return ReplyKeyboardMarkup(
        [['Прислать котика', KeyboardButton("Мои координаты", request_location=True), 'Прислать анкету']]
        )


def is_cat(file_name):
    app = ClarifaiApp(api_key=settings.API_KEY_CLARIFAI)
    model = app.public_models.general_model
    repsonse = model.predict_by_filename(file_name, max_concepts=5)

    if repsonse['status']['code'] == 10000:
        for concept in repsonse['outputs'][0]['data']['concepts']:
            if concept['name'] == 'cat':
                return True
    return False
