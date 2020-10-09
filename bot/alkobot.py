import telebot

bot = telebot.TeleBot('995067184:AAHij-PI4XB28LwRXDrrMQqKZiGY7CF7vEs')

import requests
from bs4 import BeautifulSoup


def rzhunemogu_api(type):
    const_url = 'http://rzhunemogu.ru/Rand.aspx?CType='

    r = requests.get(const_url + str(type))

    soup = BeautifulSoup(r.text, features="lxml")
    data = soup.find('content').text
    return data



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hallo')


@bot.message_handler(commands=['tost'])
def start_message(message):
    bot.send_message(message.chat.id, rzhunemogu_api(6))


@bot.message_handler(commands=['anekdot'])
def start_message(message):
    bot.send_message(message.chat.id, rzhunemogu_api(11))


bot.polling()
