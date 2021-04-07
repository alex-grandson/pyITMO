import telebot
import config
import messages
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, messages.WELCOME)


bot.polling(none_stop=True)