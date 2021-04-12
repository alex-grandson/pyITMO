import time
import random

import logging
import telebot
import config
import manager
from script.zarya01 import *

bot = telebot.TeleBot(config.TOKEN, parse_mode='HTML')
# bot = telebot.AsyncTeleBot(config.TOKEN, parse_mode='HTML')
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


def makeDelay():
    time.sleep(random.randint(1, 2) / 2)


@bot.message_handler(commands=['start'])
def send_start(message):
    for msg in START:
        if msg != START[-1]:
            bot.send_message(message.chat.id, text=msg)
        else:
            bot.send_message(message.chat.id, text=msg, reply_markup=manager.makeMarkupFromList(BUTTONS[0]))
        makeDelay()


@bot.message_handler(content_types=['voice'])
def catch_voice(message):
    bot.send_message(message.chat.id, text=MESSAGES[VOICE_MESSAGE][0],
                     reply_markup=manager.makeMarkupFromList(BUTTONS[VOICE_MESSAGE + 1]))


@bot.message_handler(content_types=['text'])
def response(message):
    print(message)
    chat_id = message.chat.id
    s = message.text
    i = -1

    for btn in BUTTONS:
        if s in btn:
            i = BUTTONS.index(btn)
            break

    if i == VOICE_MESSAGE:
        pass
    elif i == GO_AHEAD:  # Даю счет
        bot.send_message(message.chat.id, text=MESSAGES[GO_AHEAD],
                         reply_markup=manager.makeMarkupFromList(BUTTONS[GO_AHEAD + 1]))
    elif i == FORWARD_MESSAGES_I:
        makeDelay()
        bot.send_message(chat_id, MESSAGES[FORWARD_MESSAGES_I][0])
        makeDelay()
        for person in FORWARD_MESSAGES:
            bot.forward_message(chat_id, from_chat_id=person[0], message_id=person[1])
            makeDelay()
        bot.send_message(chat_id, MESSAGES[FORWARD_MESSAGES_I][1],
                         reply_markup=manager.makeMarkupFromList(BUTTONS[FORWARD_MESSAGES_I + 1]))
    elif i == LAST:
        bot.send_message(chat_id, GOODBYE)
        bot.send_sticker(chat_id, STICKER_OUT)
    elif i != -1 and s != BUTTONS[LAST]:
        for msg in MESSAGES[i]:
            isLast = msg == MESSAGES[i][-1]
            reply_markup = manager.makeMarkupFromList(BUTTONS[i + 1]) if isLast else None
            type = msg[:5]
            if type in ['audio', 'voice']:
                with open(f'./files/{type}/{msg[6:]}', 'rb') as audio:
                    bot.send_voice(chat_id, audio, reply_markup=reply_markup)
            elif type == 'video':
                with open(f'./files/{type}/{msg[6:]}', 'rb') as bubble:
                    bot.send_video_note(chat_id, bubble, reply_markup=reply_markup)
            elif type == 'photo':
                with open(f'./files/{type}/{msg[6:]}', 'rb') as photo:
                    bot.send_photo(chat_id, photo, reply_markup=reply_markup)
            elif type == 'music':
                with open(f'./files/{type}/{msg[6:]}', 'rb') as music:
                    bot.send_audio(chat_id, music, reply_markup=reply_markup)
            elif type == 'coord':
                lat, long = msg.split()[1], msg.split()[2]
                bot.send_location(chat_id, lat, long, reply_markup=reply_markup)
            else:
                bot.send_message(chat_id, text=msg, reply_markup=reply_markup)
            makeDelay()

        else:
            # TODO: обработать если сообщения кончились
            pass


bot.polling(none_stop=True)
