import telegram

def send_msg(text):
    token = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
    chat_id = "5161912359"
    bot = telegram.Bot(token=token)
    for i in text:
        bot.sendMessage(chat_id=chat_id, text=item)

item = []
with open("tgproxy.txt", 'r', encoding="utf-8") as file:
for item in file:
  send_msg(item)
