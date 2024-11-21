import telebot
from telebot import types
from quiz import TOKEN, quiz
from random import randint


bot = telebot.TeleBot(TOKEN)

user_data = {}

animals = ['жираф', 'тигровый питон', 'слон', 'капибара', 'снежный барс', 'пингвин', 'пума']



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    items1 = types.KeyboardButton('О_Московском_зоопарке')
    items2 = types.KeyboardButton('Программа_опеки')
    items3 = types.KeyboardButton('Викторина')
    items4 = types.KeyboardButton('Подобрать_тотемное_животное')
    markup.add(items1, items2, items3, items4)

    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}! Выбери интересующий пункт меню)', reply_markup=markup)


@bot.message_handler(content_types=['text', ])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'О_Московском_зоопарке':
            bot.send_message(message.chat.id, 'Московский зоопарк - один из старейших зоопарков Европы. \n'
                                              'Он был открыт 31 января 1864 года по старому стилю и назывался тогда зоосадом. \n'
                                              'Московский зоопарк был организован Императорским русским обществом акклиматизации животных и растений. \n'
                                              'Начало его существования связано с замечательными именами профессоров Московского Университета Карла Францевича Рулье, Анатолия Петровича Богданова и Сергея Алексеевича Усова\n'
                                              'Подробнее https://moscowzoo.ru/about')


        elif message.text == 'Программа_опеки':
            bot.send_message(message.chat.id, 'Основная задача Московского зоопарка с самого начала его существования это — сохранение биоразнообразия планеты. \n'
                                              'Когда вы берете под опеку животное, вы помогаете нам в этом благородном деле. \n'
                                              'При нынешних темпах развития цивилизации к 2050 году с лица Земли могут исчезнуть около 10 000 биологических видов. \n'
                                              'Московский зоопарк вместе с другими зоопарками мира делает все возможное, \n'
                                              'чтобы сохранить их... https://moscowzoo.ru/about/guardianship')


        elif message.text == 'Викторина':
            bot.send_message(message.chat.id, 'Круто!')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('Вперед!')
            back = types.KeyboardButton('Главное_меню')
            markup.add(items1, back)
            bot.send_message(message.chat.id, 'Давай пройдем викторину!', reply_markup=markup)


        elif message.text == 'Вперед!':
            user_data[message.chat.id] = {'current_question': 0, 'score': 0}
            send_question(message)

        elif message.text == 'Главное_меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('О_Московском_зоопарке')
            items2 = types.KeyboardButton('Программа_опеки')
            items3 = types.KeyboardButton('Викторина')
            items4 = types.KeyboardButton('Подобрать_тотемное_животное')
            markup.add(items1, items2, items3, items4)

            bot.send_message(message.chat.id, f'Главное_меню', reply_markup=markup)

        elif message.text == 'Подобрать_тотемное_животное':
            animal = animals[randint(0, len(animals) - 1)]
            bot.send_message(message.chat.id, f'Твое тотемное животное: ' + animal + '.')
            if animal == 'жираф':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/giraf.jpeg', 'rb'))
                bot.send_message(message.chat.id, 'Жирафы – самые высокие современные животные, что в сочетании с яркой пятнистой окраской и необычными пропорциями тела делает их абсолютно узнаваемыми.\n'
                                                  'https://moscowzoo.ru/animals/kinds/zhiraf')
            elif animal == 'слон':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/slon.jpg', 'rb'))
                bot.send_message(message.chat.id, 'Слона невозможно спутать ни с каким другим животным – серый могучий гигант с огромными ушами и хоботом – удивительным органом, аналогов которому нет в животном мире.\n'
                                                  'https://moscowzoo.ru/animals/kinds/aziatskiy_slon')
            elif animal == 'капибара':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/kapibara.jpg', 'rb'))
                bot.send_message(message.chat.id, 'Капибара — флегматичный добродушный вегетарианец, лишённый ярких индивидуальных черт, присущих некоторым его сородичам, но этот недостаток восполняется у нее спокойным и дружелюбным нравом\n'
                                                  'https://moscowzoo.ru/animals/kinds/kapibara')
            elif animal == 'тигровый питон':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/piton.jpg', 'rb'))
                bot.send_message(message.chat.id, 'Крупная неядовитая змея из рода настоящих питонов. Один из самых известных видов рода. https://moscowzoo.ru/animals/kinds/temnyy_tigrovyy_piton')

            elif animal == 'снежный барс':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/bars.jpg', 'rb'))
                bot.send_message(message.chat.id, 'Снежный барс – самая «высокогорная» кошка – живёт и охотится в одиночку в самых высоких горах мира. https://moscowzoo.ru/animals/kinds/irbis_snezhnyy_bars')

            elif animal == 'пума':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/puma.jpg', 'rb'))
                bot.send_message(message.chat.id, 'Пума включена в Международную Красную книгу как вид, чьё существование вызывает наименьшее опасение. https://moscowzoo.ru/animals/kinds/puma')

            elif animal == 'пингвин':
                chat_id = message.from_user.id
                bot.send_photo(chat_id=chat_id, photo=open('image/pingvin.jpg', 'rb'))
                bot.send_message(message.chat.id, 'У пингвинов замечательное зрение – они плохо видят ночью, но, когда светло, они прекрасно видят - как на суше, так и под водой. \n'
                                                  'https://moscowzoo.ru/animals/kinds/pingvin_gumboldta')

        else:
            handle_answer(message)


def send_question(message):
    user = user_data.get(message.chat.id)
    if user:
        question_date = quiz[user['current_question']]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for answer in question_date['answers']:
            markup.add(types.KeyboardButton(answer))
        bot.send_message(message.chat.id, question_date['question'], reply_markup=markup)


def handle_answer(message):
    user = user_data.get(message.chat.id)
    if user:
        question_data = quiz[user['current_question']]
        if message.text == question_data['correct']:
            user['score'] += 1
            bot.send_message(message.chat.id, 'Правильно!')
        else:
            bot.send_message(message.chat.id, 'Сожалею, ответ не верный. Правильный ответ: ' + question_data['correct'])

        user['current_question'] += 1
        if user['current_question'] < len(quiz):
            send_question(message)
        else:
            bot.send_message(message.chat.id, f'Викторина завершена! Ваш результат: {user["score"]} из {len(quiz)}.')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            items1 = types.KeyboardButton('Вперед!')
            items2 = types.KeyboardButton('Главное_меню')
            markup.add(items1, items2)
            bot.send_message(message.chat.id, f'Попробовать еще раз?', reply_markup=markup)
            del user_data[message.chat.id]




bot.polling(none_stop = True)