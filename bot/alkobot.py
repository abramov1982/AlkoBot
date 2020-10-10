import telebot
import bot.parcer as parcer
import json
import time

with open('token.json', 'r') as f:
    token = json.load(f)['token']

bot = telebot.TeleBot(token)

time_list = []


def timer(chat_id):
    time_list.append(chat_id)
    time.sleep(5)
    time_list.remove(chat_id)


@bot.message_handler(commands=['tost'])
def start_message(message):
    if message.chat.id not in time_list:
        bot.send_message(message.chat.id, parcer.rzhunemogu_api(6))
        timer(message.chat.id)


@bot.message_handler(commands=['anekdot'])
def start_message(message):
    if message.chat.id not in time_list:
        bot.send_message(message.chat.id, parcer.rzhunemogu_api(11))
        timer(message.chat.id)


@bot.message_handler(commands=['bash'])
def start_message(message):
    if message.chat.id not in time_list:
        bot.send_message(message.chat.id, parcer.bash_api())
        timer(message.chat.id)


@bot.message_handler(commands=['ibash'])
def start_message(message):
    if message.chat.id not in time_list:
        bot.send_message(message.chat.id, parcer.ibash_api())
        timer(message.chat.id)


bot.polling()
