import time
import random

import logging
import telebot
import config
import messages
import manager
from script.zarya01 import *

bot = telebot.TeleBot(config.TOKEN, parse_mode='HTML')
# bot = telebot.AsyncTeleBot(config.TOKEN, parse_mode='HTML')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


@bot.message_handler(commands=['start'])
def send_start(message):
    for msg in START:
        if msg != START[-1]:
            bot.send_message(message.chat.id, text=msg)
        else:
            bot.send_message(message.chat.id, text=msg, reply_markup=manager.makeMarkupFromList(BUTTONS[0]))

        time.sleep(random.randint(1, 2))


# bot.send_message(message.chat.id, MESSAGES[1], reply_markup=manager.makeMarkup(BUTTONS[0]))

@bot.message_handler(content_types=['voice'])
def catch_voice(message):
    bot.send_message(message.chat.id, text=MESSAGES[VOICE_MESSAGE][0])
    bot.send_message(message.chat.id, text=MESSAGES[VOICE_MESSAGE][1],
                     reply_markup=manager.makeMarkupFromList(BUTTONS[VOICE_MESSAGE + 1]))

@bot.message_handler(content_types=['text'])
def response(message):
    print(message)
    s = message.text
    i = -1
    for btn in BUTTONS:
        if s in btn:
            i = BUTTONS.index(btn)
            break

    if i == VOICE_MESSAGE:
        pass
    elif i == GO_AHEAD: # Даю счет
        bot.send_message(message.chat.id, text='<b>Заря 1(Каманин):</b> Давай, Юра!', reply_markup=manager.makeMarkupFromList(BUTTONS[GO_AHEAD + 1]))
    elif i == LAST:
        bot.send_message(message.chat.id, "Конец прикола! Можешь попробовать еще раз, нажав /start")
    elif i != -1 and s != BUTTONS[LAST]:
        for msg in MESSAGES[i]:
            if 'audio' in msg:
                with open(msg.split()[1], 'rb') as audio:
                    bot.send_voice(message.chat.id, audio)
            elif 'video' in msg:
                with open(msg.split()[1], 'rb') as video:
                    bot.send_video_note(message.chat.id, video)
            else:
                if msg != MESSAGES[i][-1]:
                    bot.send_message(message.chat.id, text=msg)
                else:
                    bot.send_message(message.chat.id, text=msg,
                                 reply_markup=manager.makeMarkupFromList(BUTTONS[i + 1]))
            time.sleep(random.randint(1, 2)/2)

        else:
            # TODO: обработать если сообщения кончились
            pass

bot.polling(none_stop=True)
