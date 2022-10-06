import os
import telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
# print(API_KEY)

bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(commands=['Greet'])
# def greet(message):
#     bot.reply_to(message, "Hello!")

def greet_handler(message):
    # print(message)
    if message.text == "Hello":
        # print("True")
        return True
    else:
        # print("False")
        return False

@bot.message_handler(func=greet_handler)
def greet(message):
    bot.send_message(message.chat.id, "Hello!")

bot.polling()
