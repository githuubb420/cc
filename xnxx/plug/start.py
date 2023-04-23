from telethon import events
from xnxx import xnxx


# @xnxx.register(events.NewMessage(pattern='/start'))
# async def start_handler(event):
#     await event.xnxx.send_message('Bot has been started')


@xnxx.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.reply('Howdy, how are you doing?')

@xnxx.on(events.NewMessage)
async def echo_all(event):
    await event.reply(event.text)