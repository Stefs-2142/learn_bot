import settings
import logging

from anketa import anketa_start, anketa_comment, anketa_rating, anketa_scip, anketa_name
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from handlers import greet_user, guess_number, send_cat_picture, users_coordinates, talk_to_me, check_user_photo



# Расширенное логирование, с датой и временем.
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',)

PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {
    'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    anketa = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Прислать анкету)$'), anketa_start)],
        states={
            'name': [MessageHandler(Filters.text, anketa_name)],
            'rating': [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), anketa_rating)],
            'comment': [
                CommandHandler('skip', anketa_scip),
                MessageHandler(Filters.text, anketa_comment)
            ]
            },
        fallbacks=[])

    dp = mybot.dispatcher
    dp.add_handler(anketa)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))

    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.location, users_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
