import os
import telebot
from dotenv import load_dotenv
import sqlite3
import pandas as pd
from difflib import get_close_matches

con = sqlite3.connect("qa.sqlite3")

# cur = con.cursor()

# qa_pair = cur.execute("SELECT question, answer FROM qa_pair;")
# print(qa_pair[1])

# for row in qa_pair:
#     print(row)

dataframe = pd.read_sql_query("SELECT question, answer FROM qa_pair", con)

load_dotenv()

API_KEY = os.getenv('API_KEY')
# print(API_KEY)

bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(commands=['Greet'])
# def greet(message):
#     bot.reply_to(message, "Hello!")

# def greet_handler(message):
#     # print(message)
#     if message.text == "Hello":
#         # print("True")
#         return True
#     else:
#         # print("False")
#         return False

# @bot.message_handler(func=greet_handler)
# def greet(message):
#     bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(func=lambda m: True)
def reply(message):
    q = get_close_matches(message.text,dataframe['question'])
    # print(q[0])
    ans = dataframe.loc[dataframe['question'] == q[0], 'answer'].iloc[0]
    # print(ans)
    bot.send_message(message.chat.id,ans)


bot.polling()
