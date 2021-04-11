START = [
    '<i>Заря 1: 00:00</i>\n'
    'Привет! Сегодня в мы с тобой повторим '
    'подвиг Юрия Гагарина и облетим Землю.\n'
    'Я - твой персональный помощник с Земли от программистов ИТМО.',
    'Ознакомься с позывными:\n'
    '1. Космонавт майор ГАГАРИН Ю.А.- «Кедр», телеграфом «Кдр»\n'
    '2. УКВ пункты:\n    - старт «Заря-1»\n    - Колпашево «Заря-2»\n    - Елизово «Заря-3»\n'
    '3. Все КВ центры - «Весна», телеграфом «ВСН».',
    'Как только будешь готов отправиться в полёт, отправь <b>“Как слышите меня?”</b>\n',
    'До связи!',
]
MESSAGES = [
    [
        # ['Как слышите меня?']
        'К чату присоединились:\n',
        'Председатель Государственного Комитета Совета Министров по оборонной технике <b>РУДНЕВ К.Н.</b>\n',
        'Главный конструктор ОКБ-1 <b>КОРОЛЕВ С.П.</b>\n',
        'Заместитель начальника Боевой подготовки ВВС генерал-лейтенант авиации <b>КАМАНИН Н.П.</b>\n',
        'Главный конструктор НИИ-695 <b>БЫКОВ Ю.С.</b>\n',
        'Космонавт капитан <b>ПОПОВИЧ П.Р.</b>\n',
        'Представитель ЛИИ ГКАТ <b>ГАЛАЙ М.Л.</b>',
        '<b>Заря 1 (Каманин):</b> Слышу хорошо.',
        'photo kamanin.mp4',
        '<b>Заря 1 (Каманин):</b> Как слышите меня?',
        'voice kaminin_how_u_hear.mp3'
    ],
    [
        # ['Вас слышу хорошо.']
        # через 2 минуты
        '<b>Заря 1 (Каманин):</b> Приступайте к проверке '
        '<a href="http://ru.wikipedia.org/wiki/%D0%A1%D0%9A-1_(%D1%81%D0%BA%D0%B0%D1%84%D0%B0%D0%BD%D0%B4%D1%80)">'
        'скафандра</a>. Как поняли меня?',
    ],
    [
        # ['Вас понял: приступать к проверке скафандра. Через 3 минуты. Сейчас занят.']
        '<b>Заря 1 (Каманин):</b> Вас понял.',
        '* Через 3 минуты *'
    ],
    [
        # ['ПРОВЕРИТЬ 👨‍🚀']
        '✅',
        # '*через 3 минуты*'
        '<b>Заря 1 (Каманин):</b> Проверить УКВ-связь.',
        '*отправь любое аудио-сообщение*'
    ],
    [
        # ['Как меня слышите?'] - # вместо этого отправляется ГС
        # '* через минуту *',
        '<b>Заря 1 (Каманин):</b> Слышу вас отлично, как меня слышите?',

    ],
    [
        # ['Вас слышу очень слабо, у меня горит светозвуковая передача на доске.\n']
        '<b>Заря 1 (Каманин):</b> Вас понял, слышу Вас отлично. Передача музыки идёт через 2-й КВ канал.',
        '<b>*ДЭМШ</b> – представляет собой малогабаритный шумостойкий микрофон с электромагнитными и дифференциальными '
        'характеристиками. Принцип работы заключается в преобразовании звуковых колебаний в электрические '
        'колебания звуковой частоты.'
    ],
    [
        # # ['Все сделано. Слышу вас хорошо. Работаю на ДЭМШ*. 'Даю счёт.']
        '<b>Заря 1 (Каманин):</b> Давай, Юра!'
    ],
    [
        # ['1, 2, 3, 4, 5, 6, 7, 8, 9, 10']
        '*далее в течение двух минут происходила проверка каналов связи: ДЭМШ и КВ.',
        'Команды давали друг другу отсчёт, пока настраивались каналы. Всё это время у Юрия играла музыка: '
        'Заветный перекрёсток*',
        # Зеленый перекресток
        'audio green_cross.mp3'
    ],
    [
        # ['Прием на телефон.']
        'video korolev_krudoc.mp4'
    ],
    [

        # через пару сек
        # Кедр: *включить камеру*
        'video gagarin_kedr.mp4',
        '<b>Заря 1 (Королев):</b> Как чувствуете себя, Юрий Алексеевич?'
    ],
    [
        # ['Чувствую себя превосходно. Проверка телефонов и динамиков нормально, перехожу на телефон.']
        '<b>Заря 1 (Королев):</b> Понял Вас. Дела у нас идут нормально, машина готовится нормально, '
        'все хорошо.'
    ],
    [
        # ['Понял. Я так и знал.']
        '<b>Заря 1 (Королев):</b> Понял Вас. Хорошо, все 👍'
    ],
    [
        #  ['Отправить отчёт о состоянии машины']
        '<b>Заря 1 (Королев):</b> Понял Вас отлично. <a href="https://telegra.ph/Otchet-ot-120461-04-09">'
        'Данные Ваши</a> все принял, подтверждаю. Готовность к старту принял. У нас все идет нормально.',
        # через 2 минуты
        '<b>Заря 1 (Королев):</b> Юрий Алексеевич, я хочу Вам просто напомнить, что после минутной готовности пройдет '
        'минуток шесть, прежде чем начнется 🚀. Так что Вы не волнуйтесь.'
    ],
    [
        #  ['Понял Вас. Совершенно спокоен 😌']
        '<b>Заря 1 (Королев):</b> Ну отлично, прекрасно. После минутной готовности шесть минуток будет, так сказать, '
        'всяких дел 😉 Передаю трубку председателю.',
        '*в течение двух минут Руднев справлялся о самочувствии Юрия и делился новостями*',
        'photo rudnev.mp4',
        '<b>Заря 1: (Королев):</b> Там в укладке тубы - обед, ужин и завтрак.',
        '<b>Заря 1: (Королев):</b> Колбаса, драже там и варенье к чаю. 63 штуки, будешь толстый.',
    ],
    [
        # ['😂😂😂']
        '<b>Заря 1 (Королев):</b> Сегодня прилетишь, сразу всё съешь.'
    ],
    [
        # ['Главное - колбаска есть, чтобы самогон закусывать.']
        '<b>Заря 1 (Королев):</b> Зараза, а ведь он записывает ведь всё, мерзавец!'
    ],
    [
        # ['*спеть песню*']
        # через 2 минуты
        'voice gagarin_sings.mp3',
        '<b>Заря 1 (Попович):</b> Юра, как дела?'
    ],
    [
        # ['Как учили 😂']
        '<b>Заря 1 (Попович):</b> Ну, добро, добро, давай. Ты понял, кто с тобой говорит?'
    ],
    [
        #  ['Понял - Ландыш* 😂\n* Ландышем назван космонавт Попович П. Р.']
        '<b>Заря 1 (Попович):</b> Сейчас с тобой будут говорить.',
        '<b>Заря 1 (Быков):</b> Я прошу, если у Вас есть время, подключить передатчики KB и поговорить, дать отсчет '
        'примерно до 20. Если у Вас есть время, если Вы не заняты, сообщите. Как поняли? '
        'Юра, только начинай через минуту примерно. Понял?',
        'photo bikov.mp4',
        '*далее Юрий дает отсчет для проверки канала связи КВ. А далее в течение двух минут происходит '
        'проверка положения тумблера*',
        # in 1 min
        '<b>Заря 1 (Попович):</b> Слышу тебя отлично. Юра, ты сейчас занят? 😏'
    ],
    [
        # ['Конечно, я работой не очень занят 😅']
        '<b>Заря 1 (Попович):</b> Нашел продолжение "Ландышей" 😏 Понял?'
    ],
    [
        # ['Понял, понял - продолжай.']
        '<b>Заря 1 (Попович):</b> Споем сегодня вечером.',
        # 'audio land.mp3',
        'voice whistle_landishi.mp3',
        '<b>Заря 1 (Королев):</b> У нас все идет отлично. Как чувствуете?'
    ],
    [
        # ['Вас понял. У меня тоже идет все хорошо, самочувствие хорошее, сейчас будут закрывать люк № 1.']
        # TODO: сюдазапихнуть изображение гастронома
        'video trap01.mp4',
        '*в течение трёх минут проиходила настройка связи с разной аппаратуры и проверка каналов с Быковым. Быков '
        'справлялся о самочувствии Юрия*',
    ],
    [
        '<b>Заря 1 (Галай):</b> Проверьте удобства пользования памяткой и видимость кодовой таблицы на "гастрономе". Как поняли?'
    ],
    [
        # ['Пользование памяткой и возможность считывания сигналов проверил, всё нормально.']
        '<b>Заря 1 (Попович):</b> Юра, тебе привет коллективный от всех ребят. Сейчас был у них.',
        '<b>Заря 1 (Попович):</b> Как поняли?'
    ],
    [
        # ['*насвистывать песню*'],
        'voice patch.mp3',
        'voice bunker.mp3'
    ],
    [
        '<b>Заря 1 (Королев):</b> Юрий Алексеевич, как слышите меня?'
    ],

]

BUTTONS = [
    ['Как слышите меня?'],
    ['Вас слышу хорошо.'],
    ['Вас понял: приступать к проверке скафандра. Через 3 минуты. Сейчас занят.'],
    ['ПРОВЕРИТЬ 👨‍🚀'],
    ['Как меня слышите?'],  # вместо этого отправляется ГС
    [
        'Вас слышу очень слабо, у меня горит светозвуковая передача на доске.\n'
        'Очевидно, происходит списывание с магнитофона. Как меня поняли?'
    ],
    [
        'Все сделано. Слышу вас хорошо. Работаю на ДЭМШ*. \n'
        'Даю счёт.'
    ],
    [
        '1, 2, 3, 4, 5, 6, 7, 8, 9, 10',
        'Раз, Два, Три'
    ],
    ['Прием на телефон.'],
    ['*включить камеру*'],
    ['Чувствую себя превосходно. Проверка телефонов и динамиков нормально, перехожу на телефон.'],
    ['Понял. Я так и знал.'],
    ['Отправить отчёт о состоянии машины'],
    ['Понял Вас. Совершенно спокоен 😌'],
    ['😂😂😂'],
    ['Главное - колбаска есть, чтобы самогон закусывать.'],
    ['*спеть песню*'],
    ['Как учили 😂'],
    ['Понял - Ландыш* 😂 \n* Ландышем назван космонавт Попович П. Р.'],
    ['Конечно, я работой не очень занят 😅'],
    ['Понял, понял - продолжай.'],
    ['Вас понял. У меня тоже идет все хорошо, самочувствие хорошее, сейчас будут закрывать люк № 1.'],
    ['Пользование памяткой и возможность считывания сигналов проверил, всё нормально.'],
    ['*насвистывать песню*'],
    ['Понял Вас. Большое спасибо. Передайте им самый горячий от меня🔥'],
    ['Слышу Вас хорошо, знаю, с кемв течение трёх минут проиходила нас разговариваю. 😁']

]

VOICE_MESSAGE = 4
GO_AHEAD = 6  # Даю счет
FORWARD_MESSAGES_I = 23
FORWARD_MESSAGES = [
    ['@volinov_boris', 5],  # Волынов
    ['@alexey_leonovv', 8],  # Леонов
    ['@valeriy_bikovskiy', 5],  # Быковский
    ['@victor_gorbatko', 5]  # Горбатко
]
LAST = len(BUTTONS) - 1
