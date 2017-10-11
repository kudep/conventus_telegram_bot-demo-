import configurations
import users_data
import testing_data
import os
import telebot
from telebot import types

params = configurations.get_config()
usr = users_data.UsersData(params['USERS_DB'])

print([usr.get_status(userid=1)])

bot = telebot.TeleBot(params['BOT_TOKEN'])
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('/start')
    markup.row('/menu')
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    # keyboard = types.ReplyKeyboardRemove()

@bot.message_handler(commands=['menu'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('/new_test')
    markup.row('/menu')
    bot.send_message(message.chat.id, "Your id = " + str(message.chat.id), reply_markup=markup)
    # keyboard = types.ReplyKeyboardRemove()

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)
