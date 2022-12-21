import json
import sqlite3

import telebot
from telebot import types
from string import Template

token = '5908609007:AAFryxjITAalFinxg09ekjheKMuePDkfD2Y'
bot = telebot.TeleBot(token)

api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'



class User:
    def __init__(self, fullname):
        self.fullname = fullname

        keys = ['phone', 'institute', 'thing', 'date', 'aim']

        for key in keys:
            setattr(self, key, None)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/book")
    item2 = types.KeyboardButton("/return")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет! Выбери, что тебе надо', reply_markup=markup)


@bot.message_handler(commands=['book'])
def user_reg(message):
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(message.chat.id, "Введите ФИО", reply_markup=markup)
    bot.register_next_step_handler(msg, process_fullname_step)

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        msg = bot.send_message(message.chat.id, "Введите номер телефона")
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что-то пошло не так')

def process_phone_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton('ФизМех')
        item2 = types.KeyboardButton('ГИ')
        item3 = types.KeyboardButton('ИСИ')
        item4 = types.KeyboardButton('ИММИТ')
        item5 = types.KeyboardButton('ИПМЭИТ')
        item6 = types.KeyboardButton('ИБСИБ')
        item7 = types.KeyboardButton('ИКИЗИ')
        item8 = types.KeyboardButton('ИКНТ')
        item9 = types.KeyboardButton('ИЭ')
        item10 = types.KeyboardButton('ИЭИТ')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

        msg = bot.send_message(message.chat.id, "Выберите институт", reply_markup=markup)
        bot.register_next_step_handler(msg, process_institute_step)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что-то пошло не так')

def process_institute_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.institute = message.text

        markup = types.ReplyKeyboardRemove(selective=False)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item1 = types.KeyboardButton('Колонка')
        item2 = types.KeyboardButton('Стабилизатор')

        markup.add(item1, item2)

        msg = bot.send_message(message.chat.id, "Выберите что хотите забронировать", reply_markup=markup)
        bot.register_next_step_handler(msg, process_thing_step)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что-то пошло не так')

def process_thing_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.thing = message.text

        msg = bot.send_message(message.chat.id, "Введите дату брони в формате ДД.ММ.ГГ")
        bot.register_next_step_handler(msg, process_date_step)

    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так')

def process_date_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.date = message.text

        msg = bot.send_message(message.chat.id, f"Зачем вам {user.thing}?")
        bot.register_next_step_handler(msg, process_aim_step)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что-то пошло не так')

def process_aim_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.aim = message.text

        #Ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Заявка от пользователя', message.from_user.first_name), parse_mode= "Markdown")

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что-то пошло не так')

def getRegData(user, title, name):
    t = Template('$title *$name* \n ФИО: *$fullname* \n Номер телефона: *$phone* \n Институт: *$institute* \n Предмет брони: *$thing* \n Желаемая дата: *$date* \n Цель бронирования: *$aim*')
    return t.substitute({
        'title': title,
        'name': name,
        'fullname': user.fullname,
        'phone': user.phone,
        'institute': user.institute,
        'thing': user.thing,
        'date': user.date,
        'aim': user.aim
    })

def saveData():
    connection = sqlite3.connect('book.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Book
                  (fullname TEXT, phone TEXT, institute TEXT, thing TEXT, date TEXT, aim TEXT)''')

    cursor.execute(
        "INSERT INTO Book VALUES ()")
    cursor.execute("SELECT * FROM Shows")

    print(cursor.fetchone())

    connection.commit()
    connection.close()





bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)

await client(UploadProfilePhotoRequest(
    await client.upload_file('C:\Users\sasha\pythonProject\KARELIY-0')




