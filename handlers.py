from random import choice
import os
from glob import glob

from utils import main_keyboard, get_smile, play_random_number, is_cat



def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Здравствуй, пользователь {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
    )


def send_cat_picture(update, context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_pick_file_name = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pick_file_name, 'rb'), reply_markup=main_keyboard())

def users_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Вашии координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())


def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число.'

    else:
        message = 'Введите число.'
    update.message.reply_text(message, main_keyboard())


def check_user_photo(update, context):
    update.message.reply_text("Обрабатываем фотографию.")
    os.makedirs("downloads", exist_ok=True)
    user_photo = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join("downloads", f"{user_photo.file_id}.jpg")
    user_photo.download(file_name)
    if is_cat(file_name):
        update.message.reply_text('Обнаржуен котик, добавляю в библиотеку.')
        new_file_name = os.path.join("images", f"cat_{user_photo.file_id}.jpg")
        os.rename(file_name, new_file_name)
    else:
        update.message.reply_text('Котик на фото не обнаружен :(')
        os.remove(file_name)
