import logging
import settings
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_planet(update, context):
    user_text = update.message.text
    today_data = datetime.date.today()
    planet_input = user_text.split()[-1].capitalize()
    try:
        planet = getattr(ephem,planet_input)(today_data)
        constellation = ephem.constellation(planet)
        update.message.reply_text(f'{planet_input.capitalize()} находиться в {constellation[1]} созвездии')
    except AttributeError:
        update.message.reply_text(f'Вы ввели недопустимое значение. Выберите допустимое из списка ниже:'
                                  f'\nСолнце, Меркурий, Венера, Луна, Марс, Юпитер, Сатурн, Уран, Нептун'
                                  f'\nЗапрос пишетcя на английском языке')


if __name__ == "__main__":
    main()
