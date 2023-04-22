import os
import sys
import glob
from telethon import TelegramClient, custom, events
from telethon.tl.custom import Message
from telethon.tl.types import MessageService
from pathlib import Path
from main.helper.utl import *
from . import *

print('START DEPLOY')

os.system("pip install -U telethon")

path = 'main/plug/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print('function done')
print('started')

if __name__ == "__main__":
    bot.run()
