import telegram

def send_msg(text):
    token = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
    chat_id = "5161912359"
    bot = telegram.Bot(token=token)
    for i in text:
        bot.sendMessage(chat_id=chat_id, text=line)

with open("sub-vless", 'r') as file:
  while True:
    line = file.readline()
    if not line:
        break
    send_msg(item)
