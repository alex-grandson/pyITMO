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
    'ДИСКЛЕЙМЕР: если пропала кнопка после прочтения сообщения, то снова открыть ее можно по кнопку слева от микрофона.',
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
        'Представитель ЛИИ ГКАТ <b>ГАЛЛАЙ М.Л.</b>',
        'coord 45.964443 63.305313',
        '<b>Заря 1 (Каманин):</b> Слышу хорошо.',
        'stick CAACAgIAAxkBAAECLuFgdvSNn4Hi2QRZhpVYiQIUv9SmGQACVgkAApBpuEvAK79CPW7lkh8E',  # Kamanin sticker
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
        '*отправь любое аудио-сообщение 🎤*'
    ],
    [
        # ['Как меня слышите?'] - # вместо этого отправляется ГС
        # '* через минуту *',
        '<b>Заря 1 (Каманин):</b> Слышу вас отлично, как меня слышите?',

    ],
    [
        # ['Вас слышу очень слабо, у меня горит светозвуковая передача на доске.\n']
        '<b>Заря 1 (Каманин):</b> Вас понял, слышу Вас отлично. Передача музыки идёт через 2-й КВ канал.'

    ],
    [
        # # ['Все сделано. Слышу вас хорошо. Работаю на ДЭМШ*. 'Даю счёт.']
        '<b>*ДЭМШ</b> – представляет собой малогабаритный шумостойкий микрофон с электромагнитными и дифференциальными '
        'характеристиками. Принцип работы заключается в преобразовании звуковых колебаний в электрические '
        'колебания звуковой частоты.',
        '<b>Заря 1 (Каманин):</b> Давай, Юра!'
    ],
    [
        # ['1, 2, 3, 4, 5, 6, 7, 8, 9, 10']
        '*далее в течение двух минут происходила проверка каналов связи: ДЭМШ и КВ.',
        'Команды давали друг другу отсчёт, пока настраивались каналы. Всё это время у Юрия играла музыка: '
        'Заветный перекрёсток*',
        'music zavetnii_perekrestok.mp3'
    ],
    [
        # ['Прием на телефон.']
        'video korolev_krudoc.mp4'
    ],
    [
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
        '<b>Заря 1 (Королев):</b> Понял Вас отлично. <a href="https://telegra.ph/Otchet-ot-120461-04-11">'
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
        'stick CAACAgIAAxkBAAECLuNgdvSuKr5wPF2ApVRFPgK794VW_gACeAoAArMtuEsg2oAokin5vh8E',  # rudnev stick
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
        'stick CAACAgIAAxkBAAECLuVgdvT78tvnEsZ7mR9R0VjqgMpp4wACDRAAAn2msUsIKXjwcCNEKB8E',  # bikov sticker
        '*далее Юрий дает отсчет для проверки канала связи КВ. А далее в течение двух минут происходит '
        'проверка положения тумблера*',
        # in 1 min
        '<b>Заря 1 (Попович):</b> Слышу тебя отлично. Юра, ты сейчас занят? 😏'
    ],
    [
        # ['Конечно, я работой не очень занят 😅']
        '<b>Заря 1 (Попович):</b> Нашел продолжение "Ландышей" 😉 Понял?'
    ],
    [
        # ['Понял, понял - продолжай.']
        '<b>Заря 1 (Попович):</b> Споем сегодня вечером.',
    ],
    [
        'voice whistle_landishi.mp3',
        '<b>Заря 1 (Королев):</b> У нас все идет отлично. Как чувствуете?'
    ],
    [
        # ['Вас понял. У меня тоже идет все хорошо, самочувствие хорошее, сейчас будут закрывать люк № 1.']
        # TODO: сюда запихнуть изображение гастронома
        'video trap01.mp4',
        'voice patch.mp3',
        '*в течение трёх минут проиходила настройка связи с разной аппаратуры и проверка каналов с Быковым. Быков '
        'справлялся о самочувствии Юрия*',
        'voice bunker.mp3',
        '<b>Заря 1 (Галлай):</b> Проверьте удобства пользования памяткой и видимость кодовой таблицы на '
        '"гастрономе". Как поняли?'
    ],
    [
        # ['Пользование памяткой и возможность считывания сигналов проверил, всё нормально.']
        '<b>Заря 1 (Попович):</b> Юра, тебе привет коллективный от всех ребят. Сейчас был у них.',
        '<b>Заря 1 (Попович):</b> Как поняли?'
    ],
    [
        # Понял Вас. Большое спасибо. Передайте им самый горячий от меня 🔥
        '<b>Заря 1 (Королев):</b> Юрий Алексеевич, как слышите меня?'
    ],
    [
        '<b>Заря 1 (Королев):</b> Юрий Алексеевич, я хочу Вам напомнить, что я не буду давать слово "секунды", '
        'а просто давать цифры примерно каждые полсотни, примерно: 50, 100, 150 и дальше. Понятно?'
    ],
    [
        '<b>Заря 1 (Королев):</b> Хорошо.',
        '<b>Заря 1 (Королев):</b> Юрий Алексеевич, у нас так получилось: после закрытия люка вроде один контактик 🤭 не '
        'показал, что он прижался, поэтому мы, наверное, сейчас будем снимать люк и потом его поставим снова. '
        'Как поняли меня?'
    ],
    [
        # Понял Вас правильно. Люк открыт, проверяют сигнализаторы.
        '<b>Заря 1 (Королев):</b> Ну, отлично, хорошо.',
        '<b>Заря 1 (Каманин):</b> Объявлена готовность часовая. Продолжайте осмотр оборудования. Как поняли?',
        'photo gagarin_clock.jpg',
        '<b>Заря 1 (Каманин):</b> <a href="https://telegra.ph/Paket-04-11">Пакет</a> смотрел? '
        'До него можно дотянуться? Посмотри пакет и доложи.'
    ],
    [
        # Пакет проверил. Дотянуться легко, свободно. Как поняли?
        '<b>Заря 1 (Каманин):</b> Вас понял, хорошо.'
    ],
    [
        # Кедр: У меня тоже все хорошо. Самочувствие хорошее, настроение бодрое
        '<b>Заря 1 (Королев):</b> Ну, очень хорошо. Только что справлялись из Москвы о Вашем самочувствии. '
        'Мы туда передали, что все нормально.',
        'voice moscow.mp3'
    ],
    [
        # Понял Вас
        '<b>Заря 1 (Попович):</b> Юра, ну, не скучаешь там?',
        'voice miss_us.mp3'
    ],
    [
        # Если есть музычка, можно немножко пустить.
        '<b>Заря 1 (Попович):</b> Одну минутку.',
        '<b>Заря 1 (Попович):</b> Ну, как? - Музыка есть?'
    ],
    [
        # Пока музыки нет, но, надеюсь, сейчас будет.
        '<b>Заря 1 (Попович):</b> Ну, ты слышал, как пообещали?',
        'voice promise.mp3',
        '<b>Заря 1 (Королев):</b> Ну как, музыку дали Вам, нет?'

    ],
    [
        # Пока не дали.
        '<b>Заря 1 (Королев):</b> Понятно, это же музыканты: пока туда, пока сюда, не так то быстро дело делается, '
        'как сказка сказывается, Юрий Алексеевич.'
    ],
    [
        # Дали про любовь.
        '<b>Заря 1 (Королев):</b> Дали музычку про любовь? Это толково, Юрий Алексеевич, я считаю.',
        'voice tolkovo.mp3',
        '<b>Заря 1 (Попович):</b> Юра, ну, что, дали музыку, да?'
    ],
    [
        # Музыку дали, все хорошо.
        '<b>Заря 1 (Попович):</b> Ну, добро, значит, тебе будет не так скучно.',
        'voice wont_be_missing.mp3',
        '<b>Заря 1 (Попович):</b> Юра, ребята все довольны очень тем, что у тебя все хорошо и все нормально. Понял?'
    ],
    [
        # Понял. Сердечный привет им. Слушаю Утесова. От души - "Ландыши".
        '<b>Заря 1 (Попович):</b> Ну, давай, давай, слушай.',
        # TODO: вот сюда музыку про ландыши
        'music land.mp3',
        '<b>Заря 1 (Королев):</b> Смотрели сейчас Вас по телевидению - все нормально, вид у Вас порадовал нас: бодрый. '
        'Как слышите меня?'
    ],
    [
        # Вас слышу хорошо. Самочувствие хорошее, настроение бодрое, к старту готов.
        '<b>Заря 1 (Королев):</b> Ну, отлично, хорошо. У нас идет все нормально.',
        '<b>Заря 1 (Попович):</b> Юра, ну, сейчас не скучно?'
    ],
    [
        # Хорошо. Про любовь поют там.
        '<b>Заря 1 (Попович):</b> Ну как дела, Юра? У нас все нормально, идет подготовка. Здесь хорошо идет, '
        'без всяких запинок, без всего. Ребята сейчас едут на "Зарю" ("Заря" - наземная УКВ радиостанция).'
    ],
    [
        #  Вас понял. У меня тоже все хорошо: спокоен, самочувствие хорошее. Привет ребятам.
        '<b>Заря 1 (Попович):</b> Ну, добро, добро, Юра.',
        '<b>Заря 1 (Каманин):</b> Займите исходное положение для регистрации физиологических функций.'
    ],
    [
        # Кедр: Занять исходное положение.
        'video ishodnoe_polojenie.mp4',
        '<b>Заря 1 (Каманин):</b> Сейчас будут отводить установщик. Как понял?'
    ],
    [
        # Вас понял: будут отводить установщик.
        '<b>Заря 1 (Каманин):</b> Стрела установщика отошла нормально. Как поняли?'
    ],
    [
        # Понял Вас: стрела установщика отошла нормально.
        '*ответа не последовало*'
    ],
    [
        # Как по данным медицины - сердце бьется
        '<b>Заря 1 (Каманин):</b> Пульс у Вас 64, дыхание 24. Все идет нормально.'
    ],
    [
        # Понял. Значит, сердце бьется. \nКакая сейчас готовность
        '<b>Заря 1 (Каманин):</b> 15-минутная готовность. Напоминаю: оденьте перчатки. Как поняли?',
        'photo gagarin_clock_15.jpg'
    ],
    [
        # Вас понял: 15-минутная готовность. Перчатки одел, все нормально.
        '<b>Заря 1 (Каманин):</b> Я Вас понял: передам команду. Идет перемотка ленты. Горит ли у Вас лампочка?',
        '<b>Заря 1 (Каманин):</b> Объявлена 10-минутная готовность. Как у Вас гермошлем, закрыт? Закройте гермошлем, доложите.',
        'photo gagarin_clock_10.jpg'
    ],
    [
        # Вас понял: объявлена 10-минутная готовность.
        '<b>Заря 1 (Каманин):</b> Вас понял.',
        '<b>Заря 1 (Каманин):</b> Готовность 5 мин. Поставьте громкость на полную, громкость на полную.',
        'photo gagarin_clock_5.jpg'
    ],
    [
        # Вас понял: объявлена 5-минутная готовность
        'Заря 1: Минутная готовность!',
        'voice one_minute_left.mp3',
        '<b>Заря 1 (Королев):</b> Ключ на старт!',
        '<b>Заря 1 (Королев):</b> Дается продувка.',
        'voice prodoovka.mp3'
    ],
    [
        # Понял Вас..
        'voice key_on_drenaj.mp3',
        '<b>Заря 1 (Королев):</b> Ключ поставлен на дренаж.',
        '<b>Заря 1 (Королев):</b> Все нормально: дренажные клапана закрылись.'
    ],
    [
        # Понял Вас. Настроение бодрое, самочувствие хорошее, к старту готов.
        '<b>Заря 1 (Королев):</b> Отлично.',
        '<b>Заря 1 (Королев):</b> Идут наддувы, отошла кабель-мачта, все нормально.',
        '<b>Заря 1 (Королев):</b> Дается зажигание...',
        'voice ignition.mp3'
    ],
    [
        # Понял: дается зажигание.
        'video dayo_ignition.mp4',
        '<b>Заря 1 (Королев):</b> Предварительная ступень...',
        'video prestep.mp4',
        '<b>Заря 1 (Королев):</b> Промежуточная…',
        '<b>Заря 1 (Королев):</b> Главная...',
        '<b>Заря 1 (Королев):</b> Подъем!',
        'video promejutochnaya.mp4',
        'video all_is_okay.mp4'
    ],
    [
        # Поехали!
        'video poehali.mp4',
        'video jelayo_dobrogo_poleta.mp4',
        '<b>Заря 1 (Королев):</b> 70',
        '<b>Заря 1 (Королев):</b> 100',
        '<b>Заря 1 (Королев):</b> Сброшен конус, все нормально. Как самочувствие?'
    ],
    [
        # ...Сброс головного обтекателя... Вижу Землю...
        '<b>Заря 1 (Королев):</b> Молодец, отлично! Все идет хорошо.'
    ],
    [
        # Вижу горизонт Земли. Очень такой красивый ореол
        'video rainbow.mp4',
        '<b>Заря 1 (Королев):</b> Слышим Вас отлично, продолжайте полет.'
    ],
    [
        # Полет продолжается хорошо, перегрузки растут, медленное вращение
        '<b>Заря 1:</b> Понял Вас.'
    ],
    [
        # В иллюминаторе "взора" наблюдаю Землю
        '<b>Заря 1 (Королев):</b> Все идет нормально. Вас поняли, слышим отлично.',
        '<b>Заря 1 (Каманин):</b> Все идет хорошо. Как слышите? Как самочувствие?'
    ],
    [
        # Слышу Вас отлично. Наблюдаю Землю, видимость хорошая
        'video horizont.mp4',
        '<b>Заря 1 (Каманин):</b> Вас понял, молодец! Связь отлично держите, продолжайте в том же духе.',
        'В чат зашел <i>Заря 2</i>'
    ],
    [
        # отправить данные
        '... огни ПКРС (ПКРС - прибор контроля режима спуска) горят, самочувствие хорошее, настроение бодрое.\n'
        'Параметры кабины: давление 1, влажность 65, температура 20, давление в отсеке 1, '
        'первая автоматическая 155, вторая автоматическая 155, давление в баллоне ТДУ '
        '(ТДУ - тормозная двигательная установка) 320 атмосфер...'
    ],
    [
        # @Заря3 Прием!
        'Нет сигнала.'
    ],
    [
        # @Заря3
        'Нет сигнала..'
    ],
    [
        # @Заря3 Ответьте!
        'В чат вошел <i>Заря 3</i>'
    ],
    [
        # Полет проходит успешно. Чувство невесомости
        'video nevesomost.mp4',
        '<b>Заря 3 (Карпенко):</b> Слышу Вас хорошо, приборы работают нормально, самочувствие нормальное.',
        '*Указаний от 20-го (Королева) не поступает, полет проходит нормально*',
        'coord 54.035398434070366 -164.66132197246927',
        '<b>Заря 3 (Карпенко):</b> Как Ваше самочувствие?'
    ],
    [
        # Мое самочувствие превосходное, отличное, отличное, отличное. Сообщите мне результаты о полете!
        'Заря 3 (Карпенко): Повторите, плохо слышу.'
    ],
    [
        # Чувствую себя очень хорошо, очень хорошо, хорошо.
        '*потеряна связь по УКВ каналу.*',
        'voice white_noise.mp3',
        '*Переключитесь на связь по каналу КВ*'
    ],
    [
        # выбор переключиться или вскрыть пакет
        '1. Новосибирск\n'
        'Станция работала на передачу с 9.22 до 9.39. '
        'Передавалась на борт эстрадная музыка и на фоне музыки телеграфом позывной "ВСН" через 30 секунд. '
        'Сообщений с борта не приняли.',
        '2. Алма-Ата\n'
        'Станция работала с 9.52 до 10.02 на передачу. Передавались песни Баглановой и на фоне песен '
        'телеграфом позывной "ВСН" через 30 секунд. С борта сигналов не приняли.',
        '3. Хабаровск\n'
        'Станция работала с 9.42 до 9.52 на передачу по программе. Передавались '
        '"Амурские волны" и на фоне песни телеграфом позывной "ВСН" через 30 секунд. '
        'Сигналы с борта принимались, начиная с 9.21 до 10.11 с перерывами. Двухсторонняя связь '
        'была установлена в период с 9.53 до 10.57.',
        '<b>Весна (Кадушкин):</b> Команда: КК',
        'КК - команда “сообщите контроль команд”'
    ],
    [
        # Как слышите? Передаю очередное отчетное сообщение.
        '<a href="https://telegra.ph/Otchet-04-12-2">Отчет</a>'
    ],
    [
        # 'Землю не слышу. Нахожусь в тени. Включилась солнечная ориентация'
        '<b>Весна (Кадушкин):</b> Полет проходит нормально, орбита расчетная.'
    ],
    [
        # сигнал: ОН
        'Принято, оборудование работает нормально.',
        'coord -31.60349143580783 -87.771448446172',
        '<b><i>*В эти же минуты в эфир вышло сообщение ТАСС о запуске космического корабля*</i></b>',
        'voice tass.mp3',
        '*<b>10 часов 09 минут</b> космический корабль вышел из тени Земли*',
        '*<b>10 часов 15 минут</b> Гагарин пролетал над Африкой*'
    ],
    [
        # Положить ✏️
        '✏️.',
        '✏️\n.\n.',
        '✏️\n.\n.\n.',
    ],
    [
        # *Понятно, карандаш и предметы в космосе лучше привязывать*
        '<b>10 часов 25 минут</b> включилась тормозная двигательная установка, и корабль пошел на спуск.',
        'coord 51.486816 46.211720',
        'При возвращении на Землю, во время посадки, тормозная система немного подвела и произошло '
        'небольшое отклонение от курса.',
        'coord 44.862007 37.628144',
        'На высоте семи километров в полном соответствии с планом Гагарин осуществил катапультирование, после чего '
        'модуль и космонавт в скафандре стали спускаться вниз на двух разных парашютах.',
        '<b>10 часов 55 минут</b> космонавт Юрий Гагарин приземлился в районе села Смеловка Саратовской области.',
        'photo catapoolta.jpg',
        'Длительность полёта составила <b>108 минут</b> (по другим документам - 106 минут), '
        'за это время корабль-спутник сделал один оборот вокруг земного шара.',
        'photo traektoriya.jpg',
    ],
    [
        'Регулируя парашютные стропы, космонавт смог избежать попадания в прохладные воды Волги и '
        'приземлился на берегу. Так закончился этот космический полёт.',
        'Это фото в первые минуты после приземления.',
        'photo after_landing_1.jpg',
        'А это первое, после приземления, фото с Королевым.',
        'photo after_landing_2.jpg',
        'Полёт Юрия Гагарина открыл космос для человечества.\n'
        'Как далеко мы продвинемся в космическом пространстве? '
        'К чему это приведёт? Можно только предполагать. '
        'Но, безусловно, именно благодаря полёту Юрия Гагарина '
        'стало возможным мечтать о большем.',
        'P.S. По статистике каждый пятый ребенок мечтает стать космонавтом. '
        'Не забывайте о своих мечтах, стремитесь выше звёзд! 🚀\n\n#ITMO'
    ]
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
    ['*насвистывать песню*'],
    ['Вас понял. У меня тоже идет все хорошо, самочувствие хорошее, сейчас будут закрывать люк № 1.'],
    ['Пользование памяткой и возможность считывания сигналов проверил, всё нормально.'],
    ['Понял Вас. Большое спасибо. Передайте им самый горячий от меня 🔥'],
    ['Слышу Вас хорошо, знаю, с кем разговариваю. 😁'],
    ['Понял, так я и думал'],
    ['Понял Вас правильно. Люк открыт, проверяют сигнализаторы.'],
    ['Пакет проверил. Дотянуться легко, свободно. Как поняли?'],
    ['У меня тоже все хорошо. Самочувствие хорошее, настроение бодрое.'],
    ['Понял Вас.'],
    ['Если есть музычка, можно немножко пустить.'],
    ['Пока музыки нет, но, надеюсь, сейчас будет.'],
    ['Пока не дали.'],
    ['Дали про любовь.'],
    ['Музыку дали, все хорошо.'],
    ['Понял. Сердечный привет им. Слушаю Утесова. От души - "Ландыши".'],
    ['Вас слышу хорошо. Самочувствие хорошее, настроение бодрое, к старту готов.'],
    ['Хорошо. Про любовь поют там.'],
    ['Вас понял. У меня тоже все хорошо: спокоен, самочувствие хорошее. Привет ребятам. Все время '
     'чувствую их хорошую дружескую поддержку.'],
    ['Занять исходное положение.'],
    ['Вас понял: будут отводить установщик.'],
    ['Понял Вас: стрела установщика отошла нормально.'],
    ['Как по данным медицины - сердце бьется?'],
    ['Понял. Значит, сердце бьется. \nКакая сейчас готовность?'],
    ['Вас понял: 15-минутная готовность. Перчатки одел. Магнитофон на автоматическую и ручную запись не работает. Прошу перемотать.'],
    ['Вас понял: объявлена 10-минутная готовность. Гермошлем закрыл. '
     'Все нормально, самочувствие хорошее, к старту готов.'],
    ['Вас понял: объявлена 5-минутная готовность, поставить громкость на полную.\n Полную громкость ввел.'],
    ['Понял Вас..'],
    ['Понял Вас. Настроение бодрое, самочувствие хорошее, к старту готов.'],
    ['Понял: дается зажигание.'],
    ['Поехали!'],
    ['...Сброс головного обтекателя... \nВижу Землю... \nВижу реки, складки, местности, очень хорошо у вас там видно всё!'],
    ['Вижу горизонт Земли. Очень такой красивый ореол. Сначала радуга от самой поверхности Земли, и вниз такая радуга переходит. Как слышите?'],
    ['Полет продолжается хорошо, перегрузки растут, медленное вращение, все переносится хорошо, перегрузки небольшие, самочувствие отличное.'],
    ['В иллюминаторе "взора" наблюдаю Землю: все больше закрывается облаками.'],
    ['Слышу Вас отлично. Наблюдаю Землю, видимость хорошая, различить можно все, некоторое пространство покрыто кучевой облачностью.'],
    ['отправить данные'],
    ['@Заря3 Прием!'],
    ['@Заря3'],
    ['@Заря3 Ответьте!'],
    ['Полет проходит успешно. Чувство невесомости нормально. Что можете мне сообщить?'],
    ['Мое самочувствие превосходное, отличное, отличное, отличное. Сообщите мне результаты о полете!'],
    ['Чувствую себя очень хорошо, очень хорошо, хорошо.'],
    [
        'Переключиться на связь по каналу КВ',
        'Вскрыть пакет'
    ],
    ['Как слышите? Передаю очередное отчетное сообщение.'],
    ['Землю не слышу. Нахожусь в тени. Включилась солнечная ориентация. Настроение бодрое, продолжаю полет, нахожусь над Америкой.'],
    ['сигнал: ОН'],
    ['Положить ✏️'],
    ['*Понятно, карандаш и предметы в космосе лучше привязывать*'],
    ['Приземлиться!'],
    ['Посмотрели!']
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
OPEN_PACKAGE = 64
OPEN_PACKAGE_PROBLEM = '15^2 = ?'
OPEN_PACKAGE_MESSAGE = 'Круто! Ты вышел в ручной режим. Но у нас исторический бот - в реальном полёте Юрий Алексеевич так и не распечатал пакет. Так что идём дальше...'
GOODBYE = 'Если хочешь начать заново -- жми /start, а я прощаюсь!'
STICKER_OUT = 'CAACAgIAAxkBAAECKoFgcyxcQ7SYZ3ls26If1z1TXpP_mwACkgEAAjDUnRFYJkehjKR6YB4E'
LAST = len(BUTTONS) - 1
