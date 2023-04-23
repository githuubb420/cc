import time
import redis
import logging
from telethon.sync import TelegramClient, events
from xnxx.config import *
from xnxx.helper.logger import log


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

ver = 0.1

start = '''
    bot gonna start
'''
print(start)

log.info('START SMEX')

xnxx = TelegramClient('officalcheckerbot', api_id, api_hash).start(bot_token=bot_token)


rds = redis.Redis(
    host='redis-14381.c239.us-east-1-2.ec2.cloud.redislabs.com',
    port='14381',
    password='SBtEYegaUQZu9IxGp3H8ibjGS8DObmrK'
)

if rds.ping():
    log.info("Redis Started Successfully...")

log.info(f'checker bot ver *')
log.info('bot gonna fucked')
