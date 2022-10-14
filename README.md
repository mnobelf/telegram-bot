# telegram-bot

Simple chatbot for telegram

## How To Run the API

### Ready-built docker image
1. Run on terminal :
```
docker pull nobelf27/telegram-bot:latest
```
2. Run the docker image
3. Open https://t.me/deltaku_bot on telegram

### Without using docker

1. Install dependencies, run on terminal :
```
pip3 install -r requirements.txt
```
2. Start the app, run :
```
python3 main.py
```

3. Open https://t.me/deltaku_bot on telegram

## Testing the API
The API uses package pyTelegramBotAPI as websocket technology to provide full-duplex communication.

1. Send the bot messages, the bot replies according to the question-answer pairs saved in file qa.sqlite3

    | Question | Answer   |
    | :---:   | :---: |
    | what's your name? | my name is Delta   |
    | how old are you | im 5   |
    | what is your favorite food | I love meatt   |
    | what are your hobbies? | I like sleeping a lot, eating   |
    | pizza | my favorite italian dish!   |

2. If the user does not send any messages within 10 seconds, the bot will send message "are you there?" to the user.
    it is done to prove the connection between the front and the API server is full-duplex.
