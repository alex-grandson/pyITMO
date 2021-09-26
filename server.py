import logging
import os

import aiogram.types

import dao
import manager
from bot_messages import *
import aiohttp
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

# API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

API_TOKEN = '1622184105:AAG-y-RDnbLI7Y84P-ABkOZtzwYSHOTNPUI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    id = message['from']['id']
    if dao.user_exists(id):
        lang = dao.get_lang(message.chat.id)
        print(f'User {id} exists. Lang: {lang}')
    else:
        lang = 'rus' if message['from']['language_code'] == 'ru' else 'eng'
        dao.add_user(id, lang)
        print(f'User {id} registered. Lang: {lang}')
        markup = types.ReplyKeyboardMarkup()
    for m in START[lang]:
        markup = manager.makeMarkupFromList(BUTTONS[lang][0]) if m == START[lang][-1] else None
        if m[:5] == 'photo':
            with open(f'./files/{m[:5]}/{m[6:]}', 'rb') as photo:
                await bot.send_photo(id, photo)
        else:
            await message.answer(m, reply_markup=markup)
    dao.update_plot_point(id, 1)
    print(f'{BUTTONS[lang]}')

@dp.message_handler(commands=['lang'])
async def send_lang_setup(message: types.Message):
    markup = aiogram.types.InlineKeyboardMarkup()
    markup.add(aiogram.types.InlineKeyboardButton(text='Русский 🇷🇺', callback_data='rus'))
    markup.add(aiogram.types.InlineKeyboardButton(text='English 🇬🇧', callback_data='eng'))
    await message.answer(text='Please choose language /\nПожалуйста выберете язык:', reply_markup=markup)

@dp.callback_query_handler()
async def change_language(message: types.Message):
    id = message['from']['id']
    lang = message.data
    dao.set_lang(id, lang)
    await message.answer(text=LANG_CHANGED[lang])

@dp.message_handler(content_types=['voice'])
async def react_on_voice(message: types.Message):
    id = message['from']['id']
    lang = dao.get_lang(id)
    dao.update_plot_point(id, 6)
    # dao.increase_plot_point(id)
    await message.answer(MESSAGES[lang][VOICE_MESSAGE][0],
                         reply_markup=manager.makeMarkupFromList(BUTTONS[lang][VOICE_MESSAGE]))

@dp.message_handler()
async def answer_to_user(message: types.Message):
    id = message['from']['id']
    lang = dao.get_lang(id)
    plot_point = dao.get_and_increase_plot_point(id)
    markup = aiogram.types.ReplyKeyboardMarkup()
    # if plot_point == VOICE_MESSAGE:
    #     dao.get_and_increase_plot_point(id)
    # if plot_point == GO_AHEAD:
    #     # dao.get_and_increase_plot_point(id)
    #     await message.answer(MESSAGES[lang][GO_AHEAD],
    #                       reply_markup=manager.makeMarkupFromList(BUTTONS[lang][GO_AHEAD]))
    if plot_point == FORWARD_MESSAGES_I:
        markup = manager.makeMarkupFromList(BUTTONS[lang][plot_point])
        await message.answer(MESSAGES[lang][FORWARD_MESSAGES_I][0])
        for person in FORWARD_MESSAGES[lang]:
            await bot.forward_message(id, from_chat_id=person[0], message_id=person[1])
        await message.answer(MESSAGES[lang][FORWARD_MESSAGES_I][1], reply_markup=markup)
    elif plot_point == LAST:
        await message.answer(GOODBYE[lang])
        await bot.send_sticker(id, STICKER_OUT)
        dao.update_plot_point(id, 1)

    elif plot_point < LAST:
        for m in MESSAGES[lang][plot_point]:
            needSendMarkup = m == MESSAGES[lang][plot_point][-1]
            if needSendMarkup and plot_point != VOICE_MESSAGE - 1:
                print(f'{plot_point}: {BUTTONS[lang][plot_point]}')
                markup = manager.makeMarkupFromList(BUTTONS[lang][plot_point])
            type = m[:5]
            path = f'./files/{type}/{m[6:]}'
            if type in ['audio', 'voice']:
                with open(path, 'rb') as audio:
                    await bot.send_voice(id, audio, reply_markup=markup)
            elif type == 'video':
                with open(path, 'rb') as video:
                    await bot.send_video_note(id, video, reply_markup=markup)
            elif type == 'photo':
                with open(path, 'rb') as photo:
                    await bot.send_photo(id, photo, reply_markup=markup)
            elif type == 'music':
                with open(path, 'rb') as music:
                    await bot.send_audio(id, music, reply_markup=markup)
            elif type == 'coord':
                lat, long = m.split()[1], m.split()[2]
                await bot.send_location(id, lat, long, reply_markup=markup)
            elif type == 'stick':
                stick = m.split()[1]
                await bot.send_sticker(id, stick)
            else:
                print(id, plot_point, m)
                await message.answer(m, reply_markup=markup)


executor.start_polling(dp, skip_updates=True)