from telegram import Bot, InputMediaDocument
import datetime
import pytz

BOT_TOKEN = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
CHAT_ID = -1001311543470
current_time = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))

def main():
    bot = Bot(BOT_TOKEN)
    file_paths = (
        "sub-all",
        "aktif.txt",
        "semua.txt",
        "kumpulan-p1.txt",
        "kumpulan-p2.txt",
        "kumpulan-p3.txt",
        "subapi",
        "v2tel_link.txt",
        "v2tel_links1.txt",
        "v2tel_links2.txt",
        "cm1.yml",
        "cm2.yml",
        "cm3.yml",
        "tgproxy.txt",
        "merge24.txt",
        "singbox.json",
        "nekobox.txt",
        "sub-all",
        "sub-reality",
        "sub-ss",
        "sub-trojan",
        "sub-vless",
        "sub-vmess",
        
    
    )
    for f in file_paths:
        with open(f, "rb") as fin:
            count = len(fin.readlines())
            # After the len(fin.readlines()) file's current position
            # will be at the end of the file. seek(0) sets the position
            # to the begining of the file so we can read it again during
            # sending.
            fin.seek(0)
            bot.send_document(
                CHAT_ID,
                document=fin,
                # Up to 1024 characters.
                # https://core.telegram.org/bots/api#inputmediadocument
                caption = f"Daily Update for subapi: https://api.vmess.free.nf/{f} \n\n Total Accounts: {len(fin.readlines())}\n Updated on: {current_time}"
            )

    bot.send_media_group(CHAT_ID, media=media_group)


if __name__ == "__main__":
    main()
