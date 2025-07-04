from telegram import Bot, InputMediaDocument
import datetime
import pytz

BOT_TOKEN = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
CHAT_ID = -1002292042831
current_time = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))

def main():
    bot = Bot(BOT_TOKEN)
    file_paths = (
        "ss.txt",
        "tr.txt",    
        "vl.txt",
        "vm.txt",       
    )
    # From 2 to 10 items in one media group
    # https://core.telegram.org/bots/api#sendmediagroup
    media_group = list()
    for f in file_paths:
        with open(f, "rb") as fin:
            # Up to 1024 characters.
            # https://core.telegram.org/bots/api#inputmediadocument
            caption = f"Daily Update for subapi: https://api.vmess.free.nf/{f} \n\n Total Accounts: {len(fin.readlines())}\n Updated on: {current_time}"
            # After the len(fin.readlines()) file's current position
            # will be at the end of the file. seek(0) sets the position
            # to the begining of the file so we can read it again during
            # sending.
            fin.seek(0)
            media_group.append(InputMediaDocument(fin, caption=caption))

    bot.send_media_group(CHAT_ID, media=media_group)


if __name__ == "__main__":
    main()
              
