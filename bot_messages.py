import dao
from typing import List, Dict, Tuple


def get_data(database: str, lang: str) -> List[str]:
    data = dao.fetchall(database, ['message_id', lang])
    parsed = {}
    for item in data:
        parsed[item['message_id']] = []
    for item in data:
        parsed[item['message_id']].append(item[lang])
    return parsed


START = {
    'rus': [
        '<i>Заря 1: 00:00</i>\n'
        'Привет! Сегодня в мы с тобой повторим подвиг Юрия Гагарина и облетим Землю.\n'
        'Я - твой персональный помощник с Земли от программистов ИТМО.',
        'Ознакомься с позывными:\n'
        '1. Космонавт майор ГАГАРИН Ю.А.- «Кедр», телеграфом «Кдр»\n'
        '2. УКВ пункты:\n    - старт «Заря-1»\n    - Колпашево «Заря-2»\n    - Елизово «Заря-3»\n'
        '3. Все КВ центры - «Весна», телеграфом «ВСН».',
        'Как только будешь готов отправиться в полёт, отправь <b>“Как слышите меня?”</b>\n',
        '1. TIP: если пропала кнопка ответа после прочтения сообщения, то снова открыть её можно, нажав кнопку слева от микрофона.',
        'photo btn_tip.png',
        'До связи!'],
    'eng': [
        '<i>Zarya-1: 00:00</i>\n'
        'Hi! Today, we’ll repeat Yuri Gagarin’s historical feat and orbit the Earth.\n'
        'I am your personal assistant, created by programmers from ITMO University.',
        'Here are all the call signs:\n'
        '1. Major YURI GAGARIN, cosmonaut, call sign Kedr (“Cedar pine”), Morse code KDR\n'
        '2. VHF radio stations:\n    - launch pad – Zarya-1\n    - Kolpashevo – Zarya-2\n    - Yelizovo – Zarya-3\n'
        '3. All HF radio stations: Vesna, Morse code VSN',
        'As soon as you’re ready to blast off, type  <b>“Can you hear me?”</b> in the chat.\n',
        '1. TIP: if the reply button disappears after you’ve read a message, '
        'bring it back up by tapping the square button in the tool tab.',
        'photo btn_tip.png',
        'Waiting for your command!'
    ]
}

LANG_CHANGED = {
    'rus': 'Язык успешно изменен!',
    'eng': 'Language successfully changed!'
}

CREDITS = {
    'rus':
        'Телеграм-бот создан командой #ИТМО 🚀\n\n'
        'Отдельная благодарность:\n\n'
        'Алексей Куценко - Head Developer\n'
        'Заяна Такаева- Content Manager',
    'eng':
        'Telegram bot developed by #ITMO team 🚀\n\n'
        'Special thanks:\n\n'
        'Aleksei Kutsenko - Head Developer\n'
        'Zayana Takaeva- Content Manager'
}

MESSAGES = {
    'rus': get_data('messages', 'rus'),
    'eng': get_data('messages', 'eng')
}

BUTTONS = {
    'rus': get_data('answers', 'rus'),
    'eng': get_data('answers', 'eng')
}


VOICE_MESSAGE = 5 # 5 in db
GO_AHEAD = 6  # Даю счет
FORWARD_MESSAGES_I = 24
FORWARD_MESSAGES = {
    'rus': [
        ['@volinov_boris', 5],  # Волынов
        ['@alexey_leonovv', 8],  # Леонов
        ['@valeriy_bikovskiy', 5],  # Быковский
        ['@victor_gorbatko', 5]  # Горбатко
    ],
    'eng': [
        ['@volinov_boris', 6],  # Волынов
        ['@alexey_leonovv', 9],  # Леонов
        ['@valeriy_bikovskiy', 6],  # Быковский
        ['@victor_gorbatko', 6]  # Горбатко
    ]
}
OPEN_PACKAGE = 64
OPEN_PACKAGE_PROBLEM = '15^2 = ?'
OPEN_PACKAGE_MESSAGE = {
    'rus': 'Круто! Ты вышел в ручной режим. Но у нас исторический бот - в реальном полёте Юрий Алексеевич так и не распечатал пакет. Так что идём дальше...',
    'eng': 'You’ve enabled manual controls. Awesome! But this is a historical bot, and in real life Yuri Gagarin never did unseal the envelope. So let’s move on...'
}
GOODBYE = {
    'rus': 'Если хочешь начать заново -- жми /start, а я прощаюсь!',
    'eng': 'If you want to start again, click on /start! See you!'
}
STICKER_OUT = 'CAACAgIAAxkBAAECKoFgcyxcQ7SYZ3ls26If1z1TXpP_mwACkgEAAjDUnRFYJkehjKR6YB4E'
LAST = 72