import time
import redis
from telethon.sync import TelegramClient, events
from main.config import *
from main.helper.logger import log

ver = 0.1

start = '''

    bot gonna start

'''

print(start)

log.info('START SMEX')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


start_time = time.time()

rds = redis.Redis(
    host='redis-14381.c239.us-east-1-2.ec2.cloud.redislabs.com',
    port='14381',
    password='SBtEYegaUQZu9IxGp3H8ibjGS8DObmrK'
)

if rds.ping():
    log.info("Redis Started Successfully...")

log.info(f'checker bot ver {ver}')
log.info('bot gonna fucked')
