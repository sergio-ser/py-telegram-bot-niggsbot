import telebot
from telebot import types

bot = telebot.TeleBot("823511562:AAHGKdueThEknDq_g9Bq25VVtTt2EVikeKI")
user_dict = {}

global totalAnswer
totalAnswer = 0
global questnr
questnr = 1


class User:
    def __init__(self, name):
        self.name = name
        self.points = None
        # self.sex = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global totalAnswer
    totalAnswer = 0
    msg = bot.send_message(message.chat.id,
                           "<b>Konichiwa Nigga! напиши свое имя неданиггер, посмотрим на сколько твоя жопа черная</b>", parse_mode='HTML')
    bot.register_next_step_handler(msg, get_name_quest1)


def get_name_quest1(message):
    # Get User Name and first question
    try:
        global questnr
        questnr = 1
        name = message.text
        user = User(name)
        user_dict[message.chat.id] = user
        bot.send_message(message.chat.id, 'Oк давай начнем ' + '<b>' + user.name + '</b>', parse_mode='HTML')

    except Exception as e:
        bot.send_message(message, 'oooops')

    # Question 1
    try:
        keyboard = telebot.types.InlineKeyboardMarkup()
        user = user_dict[message.chat.id]
        keyboard.row(
            telebot.types.InlineKeyboardButton(text='по имени', callback_data='по имени=0'),
            telebot.types.InlineKeyboardButton(text='ей пидар', callback_data='ей пидар=2')
        )
        bot.send_message(message.chat.id, 'Kак ты называешь своих кентов?', reply_markup=keyboard, parse_mode='HTML')

    except Exception as e:
        bot.send_message(message, 'oooops')


def thank_you(message):
    user = user_dict[message.chat.id]
    bot.send_message(message.chat.id, 'vot ona kak iobta ' + user.name)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global totalAnswer
    global questnr
    cid = call.message.chat.id
    mid = call.message.message_id
    message = call.message.text

    spl = '='
    bk_msg = call.data.split(spl, 1)[0]
    answer = call.data.split(spl, 1)[1]
    totalAnswer += int(answer)
    questnr = questnr + 1
    #print('Points = ' + str(totalAnswer))
    #print('\nquestion = ' + str(questnr))

    try:
        #question 1
        bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + '\n-----------------------------------', cid, mid)

        #question 2
        if(questnr == 2):

            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('🌿 🔽', callback_data='индика=0'),
                telebot.types.InlineKeyboardButton('☘️ 🔼', callback_data='сатива=5')
            )
            message_q = '\n-----------------------------------\nЕй! на какой картинке сатива?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)
            bot.answer_callback_query(cid, show_alert=False, text='message_q')

        #question 3
        elif(questnr == 3):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('Курева', callback_data='Курева=5'),
                telebot.types.InlineKeyboardButton('Трава', callback_data='Трава=6'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('Шмали', callback_data='Шмали=10'),
                telebot.types.InlineKeyboardButton('Наркотики', callback_data='Наркотики=0')

            )

            message_q = '\n-----------------------------------\nKак ты называешь марихуану Nigga?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)


        #question 4
        elif(questnr == 4):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('1-2', callback_data='1-2=1'),
                telebot.types.InlineKeyboardButton('3-4', callback_data='3-4=2'),
                telebot.types.InlineKeyboardButton('5-6', callback_data='5-6=3'),


            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('7', callback_data='7=5'),
                telebot.types.InlineKeyboardButton('я не курю', callback_data='я не курю=-5'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('Всю неделю, чувак', callback_data='Всю неделю, чувак=10')
            )

            message_q = '\n-----------------------------------\nСколько раз в неделе aAa?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)

        #question 5
        elif(questnr == 5):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('это хуёево', callback_data='это хуёево=5'),
                telebot.types.InlineKeyboardButton('это ахуенно', callback_data='это ахуенно=10'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('ну такое', callback_data='ну такое=1'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('это классно но стремно', callback_data='это классно но стремно=2'),
            )

            message_q = '\n-----------------------------------\nЧто ты думаешь насчет марихуаны ебана? ((только попробуй херню сморозеты ))'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)


        #question 6
        elif(questnr == 6):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('Blunt', callback_data='Blunt=6'),
                telebot.types.InlineKeyboardButton('Vadic', callback_data='Vadic=10'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('из калаша', callback_data='из калаша=0'),
                telebot.types.InlineKeyboardButton('Bong', callback_data='Bong=8'),
            )

            message_q = '\n-----------------------------------\nКак ты предпочитаешь шмалять?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)

        #question 7
        elif(questnr == 7):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('страдати херней с друзьями', callback_data='страдати херней с друзьями=10'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('играть ', callback_data='играть=2'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('Шляться', callback_data='Шляться=7'),
                telebot.types.InlineKeyboardButton('Учиться', callback_data='Учиться=0'),
            )

            message_q = '\n-----------------------------------\nКакое твое любимое занятие nigga?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)

        #question 8
        elif(questnr == 8):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('Голландия', callback_data='Голландия=7'),
                telebot.types.InlineKeyboardButton('Лос анджелес', callback_data='Лос анджелес=10'),
            )
            keyboard.row(
                telebot.types.InlineKeyboardButton('Нигерия', callback_data='Нигерия=2'),
                telebot.types.InlineKeyboardButton('Германия', callback_data='Германия=0'),
            )

            message_q = '\n-----------------------------------\nГде бы такой черномазый как ты хотел бы жить?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)

        #question 9
        elif(questnr == 9):
            keyboard = telebot.types.InlineKeyboardMarkup()

            keyboard.row(
                telebot.types.InlineKeyboardButton('Сиськи', callback_data='Сиськи=10'),
                telebot.types.InlineKeyboardButton('Жопа', callback_data='Жопа=10'),
            )

            message_q = '\n-----------------------------------\nСиськи или Жопа ?'
            bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, reply_markup=keyboard)


        #answer 10
        elif(questnr == 10):

            if(totalAnswer <= 10):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>Ооо чувак да ты просто ботаник. Иди учись!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ооо чувак да ты просто ботаник. Иди учись!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            elif(totalAnswer <= 27):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>Мне жаль, я же говорил недониггер!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Мне жаль, я же говорил недониггер!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            elif(totalAnswer <= 35):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>Мне жаль, я же говорил недониггер!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Мне жаль, я же говорил недониггер!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            elif(totalAnswer <= 47):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>А ты хорош ёпта еще немного и сможешь говорить что тебя не видно в темноте!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='А ты хорош ёпта еще немного и сможешь говорить что тебя не видно в темноте!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            elif(totalAnswer <= 54):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>А ты хорош ёпта еще немного и сможешь говорить что тебя не видно в темноте!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='А ты хорош ёпта еще немного и сможешь говорить что тебя не видно в темноте!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            elif(totalAnswer <= 58):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>Оу оу май нигга, беру слова назад твоя жопа точно черная!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Оу оу май нигга, беру слова назад твоя жопа точно черная!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            elif(totalAnswer <= 65):
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>Оу оу май нигга, беру слова назад твоя жопа точно черная!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Оу оу май нигга, беру слова назад твоя жопа точно черная!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

            else:
                message_q = '\n-----------------------------------\n\n-----------------------------------\n<b>Вывод</b>:\n<b>Ебатиииии да ты пиздишь, ты ниггер даже больше чем я тебе лечиться надо!!</b>\n<i>Если хочешь попробовать еще раз нажми или напиши /start</i>'
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ебатиииии да ты пиздишь, ты ниггер даже больше чем я тебе лечиться надо!!')
                bot.edit_message_text(message + '\nТвои ответ: ' + bk_msg + message_q, cid, mid, parse_mode="HTML")

    except:
        pass


bot.polling(none_stop=True)