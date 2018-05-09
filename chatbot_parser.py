import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests
from bs4 import BeautifulSoup
import os
import time

import telegram

# 토큰을 지정해서 bot을 선언
bot = telegram.Bot(token='xxxxxxxx')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('http://xxxxxxxxxxxxxxx')
    req.encoding = 'utf-8' # encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('#L_ > a.pjax')
    latest = posts[0].text

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            bot.sendMessage(chat_id=chat_id, text='New!!!')
            # 같은 경우는 에러 없이 넘기고, 다른 경우에만
            # 메시지 보내는 로직을 넣기
        else :
            bot.sendMessage(chat_id=chat_id, text='Nothing!!!')

        f_read.close()

        with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
            f_write.write(latest)
            f_write.close()

        time.sleep(1)
