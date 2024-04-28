import telebot
import instaloader
import time
import sqlite3
import webbrowser as wb
from telebot import types
from messages import first_text_message,second_text_message,third_text_message,fouth_text_message
from messages import back_message,front_message
from pars import formatted_info





def request_name(message):
    bot.send_message(message.chat.id, "Введите своё имя:")
    bot.register_next_step_handler(message, validate_name)

# Функция для валидации имени
def validate_name(message):
    name = message.text.strip()
    if not name.isalpha():
        bot.send_message(message.chat.id, "Имя введено некорректно. Попробуйте ещё раз.")
        request_name(message)
    else:
        

        # Подтверждаем изменения


        # Закрываем соединение с базой данных
    
        # Сохранение имени в базу данных
        # cursor.execute('UPDATE users SET name = ? WHERE user_id = ?', (name, user_id))
        # conn.commit()
        request_last_name(message)

# Функция для запроса фамилии пользователя
def request_last_name(message):
    bot.send_message(message.chat.id, "Введите свою фамилию:")
    bot.register_next_step_handler(message, validate_last_name)

# Функция для валидации фамилии
def validate_last_name(message):
    last_name = message.text.strip()
    if not last_name.isalpha():
        bot.send_message(message.chat.id, "Фамилия введена некорректно. Попробуйте ещё раз.")
        request_last_name(message)
    else:
        request_age(message)

# Функция для запроса возраста пользователя
def request_age(message):
    bot.send_message(message.chat.id, "Введите свой возраст:")
    bot.register_next_step_handler(message, validate_age)

# Функция для валидации возраста
def validate_age(message):
    age = message.text.strip()
    if not age.isdigit():
        bot.send_message(message.chat.id, "Возраст введен некорректно. Попробуйте ещё раз.")
        request_age(message)
    else:
        request_phone_number(message)

# Функция для запроса номера телефона пользователя
def request_phone_number(message):
    bot.send_message(message.chat.id, "Введите свой номер телефона:")
    bot.register_next_step_handler(message, validate_phone_number)

# Функция для валидации номера телефона
def validate_phone_number(message):
    phone_number = message.text.strip()
    if not phone_number.isdigit():
        bot.send_message(message.chat.id, "Номер телефона введен некорректно. Попробуйте ещё раз.")
        request_phone_number(message)
    else:
        bot.send_message(message.chat.id, "Регистрация успешно завершена!")




    
'====================start==========================='
bot=telebot.TeleBot("6456362724:AAHQufo9zmEWHl9QvQLi8SGhtKq1oz3B0Ms")
@bot.message_handler(commands=['start'])
def start_message_func(message):
    for el in formatted_info:
        for el2 in el.values():
            bot.send_message(message.chat.id,el2)
    # bot.send_message(message.chat.id,f'Здраствуйте {message.from_user.first_name} {message.from_user.last_name} я ваш бот консультант по выбору напраления в компании MAKERS')





    
'====================about_you=========================='    
@bot.message_handler(commands=['about_you'])
def about_you(message):
    bot.send_message(message.chat.id,f'добро пожаловать компанию  IT компанию Makers, {first_text_message}{second_text_message}{third_text_message}{fouth_text_message}')

    markup2=types.InlineKeyboardMarkup()
    btn_markup=types.InlineKeyboardButton('Хотите посмотреть на наших выпускнивов',callback_data='videos')
    btn_markup2=types.InlineKeyboardButton('Посмотреть ваш профиль в инстаграмме',callback_data='prophile')
    markup2.add(btn_markup,btn_markup2)
    bot.reply_to(message,'Отлично', reply_markup=markup2)


# video_files=[]

# @bot.callback_query_handler(func=lambda callback:True)
# def func_to_choose(callback):   
    # if callback.data=='videos':
    #     bot.send_message(callback.message.chat.id,'sdgg')
    # elif callback.data=='prophile':
    #     bot.send_message(callback.message.chat.id,'выы')




'====================get_courses====================='
@bot.message_handler(commands=['get_courses'])
def get_courses(message):
    markup=types.InlineKeyboardMarkup()
    backend_py=types.InlineKeyboardButton('Python/backend',callback_data='backend')
    frontend_js=types.InlineKeyboardButton('JavaScript/frontend',callback_data='frontend')
    markup.add(backend_py,frontend_js)
    bot.reply_to(message,'Выберите направление',reply_markup=markup)





@bot.callback_query_handler(func=lambda callback:True)
def get_courses_callback(callback):
    if callback.data=='backend':   
        Python_image=open('images/Python.svg.png','rb')
        bot.send_photo(callback.message.chat.id,Python_image)
        Python_image.close()
        bot.send_message(callback.message.chat.id,'Backend разработка — это создание скрытой от пользователя серверной части приложения, то есть логики сайта.Входе курса вы будете учить язык программирования Python (Напишите more_backend)')

    elif callback.data=='frontend':
        js_image=open('images/download.png','rb')
        bot.send_photo(callback.message.chat.id,js_image)
        js_image.close()
        bot.send_message(callback.message.chat.id,'Frontend разработка — это презентационная часть web приложений, информационной или программной системы, её пользовательский интерфейс и связанные с ним компоненты;(Напишите more_frontend)')
    elif callback.data=='videos':
        bot.send_message(callback.message.chat.id,'sdgg')
    elif callback.data=='prophile':
        bot.send_message(callback.message.chat.id,'выы')






'========================more_backend,more_frontend====================='
@bot.message_handler(commands=['more_backend','more_frontend'])
def func_more_info(message):
    if message.text=='/more_backend':
        bot.send_message(message.chat.id,{back_message})
    else:
        bot.send_message(message.chat.id,{front_message})






'========================register============================='
@bot.message_handler(commands=['register'])
def register(message):
    markup3=types.ReplyKeyboardMarkup()
    agree_button=types.KeyboardButton('Зарегестрироваться')
    disagree_button=types.KeyboardButton('Я подумаю')

    markup3.row(agree_button,disagree_button)
    bot.reply_to(message,'Хотите прийти на наши курсы?',reply_markup=markup3)
    bot.register_next_step_handler(message,register_callback)






def register_callback(message):
    if message.text=='Зарегестрироваться':
        request_name(message)
       # bot.send_message(message.chat.id,'Хорошо теперь записаны.Спасибо что выбрали Makers ')

    elif message.text=='Я подумаю':
        bot.send_message(message.chat.id,'Хорошо 15минут  часов мы вам отправим вам запрос на регистрацию')
        time.sleep(30)

        bot.reply_to(message,'Так вы готовы записаться на наши курсы')

        markup4=types.ReplyKeyboardMarkup()
        yes_button=types.KeyboardButton('Да')
        no_button=types.KeyboardButton('Нет')
        markup4.add(yes_button,no_button)

        bot.register_next_step_handler(message,decide_func)





def decide_func(message):
    if message.text=='Да':
        bot.send_message(message.chat.id,'Пройдите регистрацию')
        #get_first_name(message)
    elif message.text=='Нет':
        bot.send_message(message.chat.id,'Хорошо,мы вас поняли если передумаете,просто перезапустите бот')


bot.polling(none_stop=True)













