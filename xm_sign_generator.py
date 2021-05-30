# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import time
import hashlib
import random
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class xm_sign_generator:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'keep-alive',
            'Accept': '*/*'
        }

    def get_time(self, time_url = 'https://www.ximalaya.com/revision/time'):
        # time_url = 'https://www.ximalaya.com/revision/time'
        session = requests.session()
        response = session.get(time_url, headers=self.headers, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.text

    def get_sign(self):  # 加密值
        """
        生成 xm-sign
        规则是 md5(himalaya-服务器时间戳)(100以内随机数)服务器时间戳(100以内随机数)现在时间戳
        :return: sign
        """
        server_time = self.get_time(time_url = 'https://www.ximalaya.com/revision/time')
        now_time = str(round(time.time() * 1000))
        sign = str(hashlib.md5("himalaya-{}".format(server_time).encode()).hexdigest()) + "({})".format(
            str(round(random.random() * 100))) + server_time + "({})".format(str(round(random.random() * 100))) + now_time
        return sign

    def get_headers(self):
        sign = self.get_sign()
        self.headers["xm-sign"] = sign
        return self.headers
