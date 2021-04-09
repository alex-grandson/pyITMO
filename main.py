import time
import random
from this import s

import telebot
import config
import messages
import manager
from script import zarya01

bot = telebot.TeleBot(config.TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_start(message):
    for msg in zarya01.START:
        if msg != zarya01.START[-1]:
            bot.send_message(message.chat.id, text=msg)
        else:
            bot.send_message(message.chat.id, text=msg, reply_markup=manager.makeMarkupFromList(zarya01.BUTTONS[0]))
        time.sleep(random.randint(1, 3))


# bot.send_message(message.chat.id, zarya01.MESSAGES[1], reply_markup=manager.makeMarkup(zarya01.BUTTONS[0]))


@bot.message_handler(content_types=['text'])
def function_name(message):
    print(message)
    s = message.text
    i = -1
    for btn in zarya01.BUTTONS:
        if s in btn:
            i = zarya01.BUTTONS.index(btn)
            break
    if i != -1 and s != zarya01.BUTTONS[-1]:
        for msg in zarya01.MESSAGES[i]:
            if 'audio' in msg:
                audio = open(msg.split()[1], 'rb')
                bot.send_voice(message.chat.id, audio)
            elif 'video' in msg:
                pass
            else:
                if msg != zarya01.MESSAGES[i][-1]:
                    bot.send_message(message.chat.id, text=msg)
                else:
                    bot.send_message(message.chat.id, text=msg,
                                 reply_markup=manager.makeMarkupFromList(zarya01.BUTTONS[i + 1]))
            time.sleep(random.randint(1, 3))

        else:
            # TODO: обработать если сообщения кончились
            pass


# @bot.message_handler(regexp="SOME_REGEXP")
# def handle_message(message):
# 	pass

bot.polling(none_stop=True)
