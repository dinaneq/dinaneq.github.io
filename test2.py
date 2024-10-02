import telegram

def send_msg(text):
    token = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
    chat_id = "5161912359"
    bot = telegram.Bot(token=token)
    for i in text:
        bot.sendMessage(chat_id=chat_id, text=i)

new_list = []
with open("sub-vless", 'r', encoding="utf-8") as file:
     new_list = file.readlines()
for i in new_list:
     send_msg(i)
