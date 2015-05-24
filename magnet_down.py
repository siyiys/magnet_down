#!/usr/bin/env python
# encoding: utf-8
from u115 import API

def Geturl():
    pass

if '__name__ = main()':

    urls = Geturl()
    api = API()
    '''
    touch file ~/.115 format:
    [default]
    username = username@example.com
    password = defaultpassword

    [another]
    username = another@example.com
    password = anotherpassword
    '''
    api.login(section='default')
    if  api.has_logged_in:
        print '115已经登陆'
    else:
        print '用户名或密码错误'
    for url in urls:
        api.add_task_url(url)

