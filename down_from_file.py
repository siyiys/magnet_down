#!/usr/bin/env python
# encoding: utf-8
from u115 import API
import time
api = API()
api.login(section='default')
if  api.has_logged_in:
                print '115已经登陆'
else:
                print '用户名或密码错误'
with open(r'magnet.txt','rb') as f :
        all =f.readlines()
        for url in all:
            api.add_task_url(url)
            time.sleep(3)
api.logout()
