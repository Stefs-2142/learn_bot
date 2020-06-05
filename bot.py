import settings
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import greet_user, guess_number, send_cat_picture, users_coordinates, talk_to_me



#Расширенное логирование, с датой и временем.
logging.basicConfig(filename='bot.log', level=logging.INFO,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}




def talk_to_me(update, context):
    text = update.message.text
    print(text)
    context.user_data['emoji'] = get_smile(context.user_data)
    my_keyboard = ReplyKeyboardMarkup([['Прислать котика.']])
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())





def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))

    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, users_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

