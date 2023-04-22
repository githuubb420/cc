from telethon import events
from main import bot


@bot.register(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.bot.send_message('Bot has been started')
