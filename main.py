import time
import random

import logging
import telebot
import config
# import dao
import manager
from bot_messages import *

# bot = telebot.TeleBot(config.TOKEN, parse_mode='HTML')
bot = telebot.AsyncTeleBot(config.TOKEN, parse_mode='HTML')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.


def makeDelay():
    time.sleep(random.randint(1, 2) / 2)


@bot.message_handler(commands=['start'])
def send_start(message):
    id = message.chat.id
    if dao.user_exists(id):
        lang = dao.get_lang(message.chat.id)
        print(f'User {id} exists. Lang: {lang}')
    else:
        lang_id = str(message).find('language_code') + 17
        lang = 'rus' if str(message)[lang_id:lang_id + 2] == 'ru' else 'eng'
        print(f'User {id} registered. Lang: {lang}')
        dao.add_user(id, lang)
    for msg in START[lang]:
        reply_markup = manager.makeMarkupFromList(BUTTONS[lang][0]) if msg == START[lang][-1] else None
        if msg[:5] == 'photo':
            with open(f'./files/{msg[:5]}/{msg[6:]}', 'rb') as photo:
                bot.send_photo(message.chat.id, photo, reply_markup=reply_markup)
        else:
            bot.send_message(message.chat.id, text=msg, reply_markup=reply_markup)
        makeDelay()
    dao.update_plot_point(id, 1)


@bot.message_handler(commands=['lang'])
def send_change_lang(message: telebot.types.Message):
    id = message.chat.id
    markup = manager.makeChangeLangMarkup()
    bot.send_message(id, 'Смена языка / Change language:', reply_markup=markup)


def change_lang(callback: telebot.types.CallbackQuery):
    print(callback.data)
    print(callback.message.chat.id)
    id = callback.message.chat.id
    lang = dao.get_lang(id)
    dao.set_lang(id, lang)
    bot.send_message(callback.message.chat.id, text=CHANGE_LANG[lang])


@bot.callback_query_handler(change_lang)
def send_change_lang_result(message):
    pass


@bot.message_handler(commands=['credits'])
def send_credits(message: telebot.types.Message):
    lang = dao.get_lang(message.chat.id)
    bot.send_message(message.chat.id, text=CREDITS[lang])


@bot.message_handler(content_types=['voice'])
def catch_voice(message: telebot.types.Message):
    id = message.chat.id
    plot_point = dao.get_plot_point(id)
    lang = dao.get_lang(id)
    bot.send_message(message.chat.id, text=MESSAGES[lang][VOICE_MESSAGE][0],
                     reply_markup=manager.makeMarkupFromList(BUTTONS[lang][VOICE_MESSAGE + 1]))


@bot.message_handler(regexp='Вскрыть пакет')
def open_package(message: telebot.types.Message):
    bot.send_message(message.chat.id, OPEN_PACKAGE_PROBLEM)


@bot.message_handler(regexp='225')
def open_package(message):
    makeDelay()
    bot.send_message(message.chat.id, OPEN_PACKAGE_MESSAGE,
                     reply_markup=manager.makeMarkupFromList(BUTTONS[OPEN_PACKAGE + 1]))
    makeDelay()
    for msg in MESSAGES[OPEN_PACKAGE]:
        bot.send_message(message.chat.id, msg)
        makeDelay()


@bot.message_handler(content_types=['text'])
def response(message):
    id = message.chat.id
    plot_point = dao.get_plot_point(id)
    dao.get_and_increase_plot_point(id)
    lang = dao.get_lang(id)

    print('Response for: ', id, lang, plot_point)

    if plot_point == VOICE_MESSAGE:
        pass
    elif plot_point == GO_AHEAD:  # Даю счет
        bot.send_message(message.chat.id, text=MESSAGES[lang][GO_AHEAD],
                         reply_markup=manager.makeMarkupFromList(BUTTONS[GO_AHEAD + 1]))
    elif plot_point == FORWARD_MESSAGES_I:
        makeDelay()
        bot.send_message(id, MESSAGES[FORWARD_MESSAGES_I][0])
        makeDelay()
        for person in FORWARD_MESSAGES:
            bot.forward_message(id, from_chat_id=person[0], message_id=person[1])
            makeDelay()
        bot.send_message(id, MESSAGES[FORWARD_MESSAGES_I][1],
                         reply_markup=manager.makeMarkupFromList(BUTTONS[FORWARD_MESSAGES_I + 1]))
    elif plot_point == LAST:
        bot.send_message(id, GOODBYE)
        bot.send_sticker(id, STICKER_OUT)
    elif plot_point < 72:
        for msg in MESSAGES[lang][plot_point]:
            print(msg)
            isLast = msg == MESSAGES[lang][plot_point][-1]
            reply_markup = manager.makeMarkupFromList(BUTTONS[lang][plot_point + 1]) if isLast else None
            if plot_point == VOICE_MESSAGE: reply_markup = None
            type = msg[:5]
            if type in ['audio', 'voice']:
                with open(f'./files/{type}/{msg[6:]}', 'rb') as audio:
                    bot.send_voice(id, audio, reply_markup=reply_markup)
            elif type == 'video':
                with open(f'./files/{type}/{msg[6:]}', 'rb') as bubble:
                    bot.send_video_note(id, bubble, reply_markup=reply_markup)
            elif type == 'photo':
                with open(f'./files/{type}/{msg[6:]}', 'rb') as photo:
                    bot.send_photo(id, photo, reply_markup=reply_markup)
            elif type == 'music':
                with open(f'./files/{type}/{msg[6:]}', 'rb') as music:
                    bot.send_audio(id, music, reply_markup=reply_markup)
            elif type == 'coord':
                lat, long = msg.split()[1], msg.split()[2]
                bot.send_location(id, lat, long, reply_markup=reply_markup)
            elif type == 'stick':
                stick = msg.split()[1]
                bot.send_sticker(id, stick)
            else:
                bot.send_message(id, text=msg, reply_markup=reply_markup)

            makeDelay()

        else:
            # TODO: обработать если сообщения кончились
            pass


bot.polling(none_stop=True)
