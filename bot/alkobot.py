import telebot
import parcer.parcer as parcer
import json
import time

with open('token.json', 'r') as f:
    token = json.load(f)['token']

bot = telebot.TeleBot(token)
time_list = []
chats_ids = [-1001206122362, -1001409669768]


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/bash', '/ibash')
keyboard1.row('/tost', '/anekdot')


def timer(chat_id):
    time_list.append(chat_id)
    time.sleep(5)
    time_list.remove(chat_id)


@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери', reply_markup=keyboard1)


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


@bot.message_handler(regexp='^[т][о]*[л][я]*?[н]?[и]?[к]?[, ]?[ ]?[ст][ко][алс][жкт][ину]?[ий]?\s?[т]?[о]?[с]?[т]?$')
def handle_message(message):
    if message.chat.id in chats_ids:
        bot.send_message(message.chat.id, parcer.rzhunemogu_api(6))
        timer(message.chat.id)


bot.polling()
