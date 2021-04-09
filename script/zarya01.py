START = [
    '<i>Заря 1: 00:00</i>\n'
    'Привет! Сегодня в мы с тобой повторим '
    'подвиг Юрия Гагарина и облетим Землю.\n'
    'Я - твой персональный помощник с Земли, так что будь на связи.\n',
    'Как только будешь готов отправиться в полёт, отправь <b>“Как слышите меня?”</b>\n',
    'До связи!',
]
MESSAGES = [
    [
        'К чату присоединились:\n',
        'Председатель Государственного Комитета Совета Министров по оборонной технике <b>РУДНЕВ К.Н.</b>\n',
        'Главный конструктор ОКБ-1 <b>КОРОЛЕВ С.П.</b>\n',
        'Заместитель начальника Боевой подготовки ВВС генерал-лейтенант авиации <b>КАМАНИН Н.П.</b>\n',
        'Главный конструктор НИИ-695 <b>БЫКОВ Ю.С.</b>\n',
        'Космонавт капитан <b>ПОПОВИЧ П.Р.</b>\n',
        'Представитель ЛИИ ГКАТ <b>ГАЛАЙ М.Л.</b>',
        # ],
        # [
        'Заря 1 (Каманин): Слышу хорошо.',
        'Заря 1 (Каманин): Как слышите меня?'
    ],
    [
        # через 2 минуты
        'Заря 1 (Каманин): Приступайте к проверке <a href="https://ru.wikipedia.org/wiki/Скафандр">скафандра</a>. Как поняли меня?',
    ],
    [
        'Заря 1 (Каманин): Вас понял.'
    ],
    [
        '✅',
        # '*через 3 минуты*'
        'Заря 1(Каманин): Проверить УКВ-связь.'
    ],
    [
        # '* через минуту *',
        'Заря 1(Каманин): Слышу вас отлично, как меня слышите?',
        'Заря 1 (Каманин): Вас понял, слышу Вас отлично. Передача музыки идёт через 2-й КВ канал.'
    ],
    [
        '*ДЭМШ – представляет собой малогабаритный шумостойкий микрофон с электромагнитными и дифференциальными '
        'характеристиками. Принцип работы заключается в преобразовании звуковых колебаний в электрические '
        'колебания звуковой частоты.'
    ],
    [
        '*далее в течении двух минут происходила проверка каналов связи: ДЭМШ и КВ. '
        'Команды давали друг другу отсчёт, пока настраивались каналы. Всё это время у Юрия играла музыка: '
        'Заветный перекрёсток*',
        # Зеленый перекресток
        'audio ./files/audio/01_green_cross.mp3',
        # через пару сек
        'Заря 1 (Королев): Как чувствуете себя, Юрий Алексеевич?'
    ],
    [
        'Заря 1 (Королев): Понял Вас. Дела у нас идут нормально, машина готовится нормально, '
        'все хорошо.'
    ],
    [
        'Заря 1 (Королев): Понял Вас. Хорошо, все 👍'
    ]
]

BUTTONS = [
    'Как слышите меня?',
    'Вас слышу хорошо.',
    'Вас понял: приступать к проверке скафандра. Через 3 минуты. Сейчас занят.',
    'ПРОВЕРИТЬ 👨‍🚀',
    'Как меня слышите?',
    'Вас слышу очень слабо, у меня горит светозвуковая передача на доске.\n'
    'Очевидно, происходит списывание с магнитофона. Как меня поняли?',
    'Все сделано. Слышу вас хорошо. Работаю на ДЭМШ*.\n\nДаю счёт.',
    [
        '1, 2, 3, 4, 5, 6, 7, 8, 9, 10',
        'Раз, Два, Три'
    ],
    'Чувствую себя превосходно. Проверка телефонов и динамиков нормально, перехожу на телефон.',
    'Понял. Я так и знал.'

]

# DICT = dict(zip(USER_ANSWERS, BOT_ANSWERS))
