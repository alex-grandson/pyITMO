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
        bot.send_sticker(chat_id, 'CAACAgIAAxkBAAECKoFgcyxcQ7SYZ3ls26If1z1TXpP_mwACkgEAAjDUnRFYJkehjKR6YB4E')
        bot.send_message(chat_id, "Конец прикола! Можешь попробовать еще раз, нажав /start")
    elif i != -1 and s != BUTTONS[LAST]:
        for msg in MESSAGES[i]:
            isLast = msg == MESSAGES[i][-1]
            markup = manager.makeMarkupFromList(BUTTONS[i + 1]) if isLast else None
            if msg[:5] in ['audio', 'voice']:
                with open(f'./files/{msg[:5]}/{msg[6:]}', 'rb') as audio:
                    bot.send_voice(chat_id, audio, reply_markup=markup)
            elif msg[:5] in ['video', 'photo']:
                with open(f'./files/{msg[:5]}/{msg[6:]}', 'rb') as bubble:
                    bot.send_video_note(chat_id, bubble, reply_markup=markup)
            elif msg[:5] == 'music':
                with open(f'./files/{msg[:5]}/{msg[6:]}', 'rb') as music:
                    bot.send_audio(chat_id, music, reply_markup=markup)
            else:
                bot.send_message(chat_id, text=msg, reply_markup=markup)
            makeDelay()

        else:
            # TODO: обработать если сообщения кончились
            pass


bot.polling(none_stop=True)
