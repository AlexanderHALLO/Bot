import telebot
import webbrowser
from telebot import types


# Токен бота с которым работаем
bot = telebot.TeleBot('7489393124:AAGQjg5eSm14XW_vhTyNr8mUN6tdTowXe4o')


# задаем команды
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://vk.com/linkforme')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Дороу, {message.from_user.first_name} {message.from_user.last_name})))')


@bot.message_handler(commands=['help'])
def main(message):


    # создаем кнопочки
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Признание в слабости', url='https://vk.com/linkforme'))
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Узнать себя в ТГ', url='https://vk.com/linkforme'))
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Посмотреть на создателя', url='https://vk.com/linkforme'))
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Все по новой', url='https://vk.com/linkforme'))


    bot.send_message(message.chat.id, '<em>Помощь</em> <b><u>дауничу</u></b> ...'
                                      'Список комманд:'
                                      ' <b>/help</b>,  '
                                      ' <b>/id</b>,  '
                                      ' <b>/site</b>,  '
                                      '<b>/start</b>  ', parse_mode='html')


@bot.message_handler(commands=['id'])
def main(message):
    bot.reply_to(message, f'id: {message.from_user.id}')


# обработка файлов типа фото и тд
@bot.message_handler(content_types=['photo'])
def get_content(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посмотри кто это со мной так...', url='https://vk.com/linkforme'))
    bot.reply_to(message, 'Сорян я в душе не ебу что ты отправил....', reply_markup=markup)


# обработка текса и вывод соотв команд
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Дороу, {message.from_user.first_name} {message.from_user.last_name})))')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id: {message.from_user.id}')


bot.infinity_polling()
