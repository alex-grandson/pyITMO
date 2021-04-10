import time
import random

import logging
import telebot
import config
import messages
import manager
from script import zarya01

bot = telebot.TeleBot(config.TOKEN, parse_mode='HTML')
# bot = telebot.AsyncTeleBot(config.TOKEN, parse_mode='HTML')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


@bot.message_handler(commands=['start'])
def send_start(message):
    for msg in zarya01.START:
        if msg != zarya01.START[-1]:
            bot.send_message(message.chat.id, text=msg)
        else:
            bot.send_message(message.chat.id, text=msg, reply_markup=manager.makeMarkupFromList(zarya01.BUTTONS[0]))

        time.sleep(random.randint(1, 2))


# bot.send_message(message.chat.id, zarya01.MESSAGES[1], reply_markup=manager.makeMarkup(zarya01.BUTTONS[0]))

@bot.message_handler(content_types=['voice'])
def catch_voice(message):
    bot.send_message(message.chat.id, text=zarya01.MESSAGES[4][0])
    bot.send_message(message.chat.id, text=zarya01.MESSAGES[4][1],
                     reply_markup=manager.makeMarkupFromList(zarya01.BUTTONS[5]))

@bot.message_handler(content_types=['text'])
def response(message):
    print(message)
    s = message.text
    i = -1
    for btn in zarya01.BUTTONS:
        if s in btn:
            i = zarya01.BUTTONS.index(btn)
            break

    if i == 4: # для ГС
        pass
    elif i == 6: # даю счет
        bot.send_message(message.chat.id, text='<b>Заря 1(Каманин):</b> Давай, Юра!', reply_markup=manager.makeMarkupFromList(zarya01.BUTTONS[7]))
    elif i == len(zarya01.BUTTONS) - 1:
        bot.send_message(message.chat.id, "Конец прикола! Можешь попробовать еще раз, нажав /start")
    elif i != -1 and s != zarya01.BUTTONS[-1]:
        for msg in zarya01.MESSAGES[i]:
            if 'audio' in msg:
                with open(msg.split()[1], 'rb') as audio:
                    bot.send_voice(message.chat.id, audio)
            elif 'video' in msg:
                with open(msg.split()[1], 'rb') as video:
                    bot.send_video_note(message.chat.id, video)
            else:
                if msg != zarya01.MESSAGES[i][-1]:
                    bot.send_message(message.chat.id, text=msg)
                else:
                    bot.send_message(message.chat.id, text=msg,
                                 reply_markup=manager.makeMarkupFromList(zarya01.BUTTONS[i + 1]))
            time.sleep(random.randint(1, 2)/2)

        else:
            # TODO: обработать если сообщения кончились
            pass

bot.polling(none_stop=True)
