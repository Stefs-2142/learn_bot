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
    return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton("Мои координаты", request_location=True)]]) 