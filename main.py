import os
import telebot
from dotenv import load_dotenv
import sqlite3
import pandas as pd
from difflib import get_close_matches
import time
import threading

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

last_messages = []
waiting_time = 5

@bot.message_handler(func=lambda m: True)
def reply(message):
    q = get_close_matches(message.text,dataframe['question'])
    # print(q[0])
    ans = dataframe.loc[dataframe['question'] == q[0], 'answer'].iloc[0]
    # print(ans)
    print(message)
    bot.send_message(message.chat.id,ans)

    # check if there's no {message.chat.username} in last_messages[] then append to last_messages[]
    found = False
    for m in last_messages:
        if m.chat.username == message.chat.username:
            last_messages.remove(m)
            last_messages.append(message)
            found = True
    
    if not(found):
        last_messages.append(message)


#always check for all member of last_messages[], if message.date + 5 < time.now(), then send_message to the message.chat.id and delete it from last_messages[]
def idle_check_thread():
    # global last_msg
    # global waiting_time
    while True:
        current_time = time.time()
        try:
            for m in last_messages:
                if (m.date + waiting_time) < current_time:
                    bot.send_message(m.chat.id,"are you there?")
                    last_messages.remove(m)
        except:
            pass

x = threading.Thread(target=idle_check_thread)
x.start()


bot.polling()
