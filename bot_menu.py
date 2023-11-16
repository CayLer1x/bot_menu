import telebot
import os
import random
from telebot import types
# Getting Bot Token From Secrets
BOT_TOKEN = '6654572893:AAFDNNtyUqBA3DSVGxg9A6bPudpxJKsi9x0'
# Creating Telebot Object
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
    bot.send_message(message.chat.id, 'Чтобы ознакомиться с командами напишите /help')


@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, '''Мои Команды:
Вызвать меню: /menu
Отправить локацию: /location
Отправить Песню: /song
Отправить Видео: /video
Увидеть Кружочек: /meme
1 Случайный Пароль: /password   ''')
#-------------------------------------------------------------------Генератор паролей
@bot.message_handler(commands=['password'])
def location(message):
    A = "QWERTYUIOPASDFGHJKLZXCVBNM"
    a = A.lower()
    numbers = '1234567890'
    sumbols = "()[]{}.;,/\\?=+ _"

    upper, lower, nums, syms = True, True, True, False

    all = ""

    if upper:
        all += A
    if lower:
        all += a
    if nums:
        all += numbers
    if syms:
        all += sumbols

    length = 20
    amount = 10
    bot.send_message(message.from_user.id,  f'Вот вам Пароли: ')
    for x in range(amount):
        password = ''.join(random.sample(all, length))
        bot.send_message(message.from_user.id, password)
        print(password)
    
#------------------------------------------------------------------ Остальные команды
@bot.message_handler(commands=['location'])
def location(message):
    bot.send_message(message.from_user.id,  text='Вот вам адрес Шашлычной')
    bot.send_location(message.from_user.id, 43.21832483103529, 76.88650014523766)

@bot.message_handler(commands=['song'])
def song(message):
    audio = open(r'C:\Users\Admin\Desktop\python_work\pythonbots\menu_bot\Jonjthan Idyll.mp3', 'br')
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['video'])
def video(message):
    video_path = r'C:\Users\Admin\Desktop\python_work\pythonbots\menu_bot\TitleRobert.mp4'
    video = open(video_path, 'rb')
    bot.send_video(message.chat.id, video, timeout=15)

@bot.message_handler(commands=['meme'])
def meme(message):
    image_path = r'C:\Users\Admin\Desktop\python_work\pythonbots\menu_bot\qewrew.mp4'
    meme = open(image_path, 'rb')
    bot.send_video_note(message.chat.id, meme, duration=10)
#------------------------------------------------------------------------------------MENU BUTTONS
@bot.message_handler(commands=['menu'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🔅 Рандомное число')
        key3 = types.KeyboardButton('➡️ Другое')
        markup.add(key1,key3)
        bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == '🔅 Рандомное число':
        bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 100000)))


    elif message.text == '➡️ Другое':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🤖 Полная инфа о боте')
        key2 = types.KeyboardButton('🐱 Хочу увидеть котиков')
        back = types.KeyboardButton('◀️ Назад')
        markup.add(key1,key2,back)
        bot.send_message(message.chat.id, '➡️ Другое'.format(message.from_user), reply_markup=markup)

    elif message.text == '🐱 Хочу увидеть котиков':
        cats = ['https://rabotatam.ru/uploads/monthly_2017_04/large.58f1bdeda1c5c_.jpg.91c33c120ad86a4dbf2c50dd44d00890.jpg', 
                'https://w.forfun.com/fetch/ef/ef5d5a59c4a4d9d1deb9a3722b744951.jpeg', 
                'https://chudo-prirody.com/uploads/posts/2021-08/1628905019_37-p-skachat-foto-milikh-kotikov-41.jpg',
                ]
        random_index = cats[random.randint(0, len(cats) - 1)]
        bot.send_message(message.chat.id, 'Ваш котик:')
        bot.send_photo(message.chat.id, random_index)
    
    elif message.text == '🤖 Полная инфа о боте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🔅 Рандомное число')
        key3 = types.KeyboardButton('➡️ Другое')
        markup.add(key1,key3)
        name = bot.get_me()
        bot.send_message(message.chat.id, f'Моя информация:\n{name}', reply_markup=markup)
         
    
    elif message.text == '◀️ Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🔅 Рандомное число')
        key3 = types.KeyboardButton('➡️ Другое')
        markup.add(key1,key3)
        bot.send_message(message.chat.id, '◀️ Назад'.format(message.from_user), reply_markup=markup)      



bot.polling()
