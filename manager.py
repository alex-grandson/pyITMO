import aiogram.types
from aiogram import types
from typing import List

inline_markup = types.InlineKeyboardMarkup()
markup = types.ReplyKeyboardMarkup()


def makeMarkupFromList(buttons: List[str]):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for btn in buttons:
        markup.add(aiogram.types.InlineKeyboardButton(btn))
        # markup.add(types.KeyboardButton(btn))
    # markup = types.ReplyKeyboardRemove(selective=False)
    markup.one_time_keyboard = True
    return markup


def makeChangeLangMarkup():
    inline_markup.add(types.InlineKeyboardButton('🇷🇺 RUS', callback_data='rus'))
    inline_markup.add(types.InlineKeyboardButton('🇬🇧 ENG', callback_data='eng'))
    return inline_markup


def makeMarkup(btn: str):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(types.KeyboardButton(btn))
    markup.one_time_keyboard = True
    return markup
