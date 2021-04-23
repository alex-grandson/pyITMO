import telebot
from telebot import types


def makeMarkupFromList(buttons: list):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for btn in buttons:
        markup.add(types.KeyboardButton(btn))
    # markup = types.ReplyKeyboardRemove(selective=False)
    markup.one_time_keyboard=True
    return markup


def makeMarkup(btn: str):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(types.KeyboardButton(btn))
    markup.one_time_keyboard=True
    return markup


def checkLanguage(message):
    return message.user.language_code