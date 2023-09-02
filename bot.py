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
    planet_input = user_text.split()[-1].lower()

    planet = {
        'jupiter': ephem.Jupiter(today_data),
        'mars': ephem.Mars(today_data),
        'mercury': ephem.Mercury(today_data),
        'moon': ephem.Moon(today_data),
        'neptune': ephem.Neptune(today_data),
        'saturn': ephem.Saturn(today_data),
        'sun': ephem.Sun(today_data),
        'uranus': ephem.Uranus(today_data),
        'venus': ephem.Venus(today_data),

        'юпитер': ephem.Jupiter(today_data),
        'марс': ephem.Mars(today_data),
        'меркурий': ephem.Mercury(today_data),
        'луна': ephem.Moon(today_data),
        'нептун': ephem.Neptune(today_data),
        'сатурн': ephem.Saturn(today_data),
        'солнце': ephem.Sun(today_data),
        'уран': ephem.Uranus(today_data),
        'венера': ephem.Venus(today_data),
    }

    if planet_input in planet:
        constellation = ephem.constellation(planet[planet_input])
        update.message.reply_text(f'{planet_input.capitalize()} находиться в {constellation[1]} созвездии')
    else:
        update.message.reply_text(f'Вы ввели недопустимое значение. Выберите допустимое из списка ниже:'
                                  f'\nСолнце, Меркурий, Венера, Луна, Марс, Юпитер, Сатурн, Уран, Нептун')


if __name__ == "__main__":
    main()
