import asyncio
import telegram

TOKEN = "YOUR_BOT_TOKEN"
chat_id = 'CHAT_ID_OR_CHANNEL_ID'

bot = telegram.Bot(token=TOKEN)
async def send_document(document, chat_id):
    async with bot:
        await bot.send_document(document=document, chat_id=chat_id)

async def main():
  
    # Sending a document
    await send_document(document=open('/path/to/document.pdf', 'rb'), chat_id=chat_id)

if __name__ == '__main__':
    asyncio.run(main())
