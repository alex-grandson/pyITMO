import telebot
from telebot import types


def makeMarkup(buttons: list):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for btn in buttons:
        markup.add(types.KeyboardButton(btn))
    # markup = types.ReplyKeyboardRemove(selective=False)
    return markup


def makeMarkup(btn: str):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(types.KeyboardButton(btn))
    return markup