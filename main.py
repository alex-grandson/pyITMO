import telebot
import config
import messages
import manager
from script import zarya01

bot = telebot.TeleBot(config.TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_start(message):
	bot.send_message(message.chat.id, zarya01.MESSAGES[0])
	bot.send_message(message.chat.id, zarya01.MESSAGES[1], reply_markup=manager.makeMarkup(zarya01.USER_ANSWERS[0]))

@bot.message_handler(content_types=['text'])
def function_name(message):
	s = message.text
	if s in zarya01.USER_ANSWERS:
		i = zarya01.USER_ANSWERS.index(s)
		if s != zarya01.USER_ANSWERS[-1]:
			bot.send_message(message.chat.id, zarya01.DICT[s], reply_markup=manager.makeMarkup(zarya01.USER_ANSWERS[i + 1]))
		else:
			# TODO: обработать если сообщения кончились
			pass
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

bot.polling(none_stop=True)