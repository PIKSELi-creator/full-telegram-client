from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
session_string = os.getenv('SESSION_STRING')  # optional

client = TelegramClient(
    StringSession(session_string) if session_string else 'full_telegram_client',
    api_id,
    api_hash
)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Привет! Это полноценный Telegram клиент 🚀\nНапиши /help')

@client.on(events.NewMessage(pattern='/help'))
async def help_cmd(event):
    await event.reply('Команды:\n/start - приветствие\n/ping - тест\n/info - информация об аккаунте')

@client.on(events.NewMessage(pattern='/ping'))
async def ping(event):
    await event.reply('Pong! 🏓')

@client.on(events.NewMessage(pattern='/info'))
async def info(event):
    me = await client.get_me()
    await event.reply(f'👤 **{me.first_name}**\nID: {me.id}\nUsername: @{me.username}')

# Обработчик всех сообщений
@client.on(events.NewMessage())
async def echo(event):
    if event.is_private and not event.message.text.startswith('/'):
        await event.reply(f'Ты сказал: {event.message.text}')

async def main():
    await client.start()
    print('Клиент запущен...')
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())