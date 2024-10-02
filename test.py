import asyncio
import telegram

TOKEN = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
chat_id = '5161912359'

bot = telegram.Bot(token=TOKEN)
async def send_document(document, chat_id):
    async with bot:
        await bot.send_document(document=document, chat_id=chat_id)

async def main():
  
    # Sending a document
    await send_document(document=open('/sub-all', 'rb'), chat_id=chat_id)

if __name__ == '__main__':
    asyncio.run(main())
