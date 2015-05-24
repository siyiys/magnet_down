#!/usr/bin/env python
# encoding: utf-8

from getdown import getInfo
from u115 import API
import time

def first():
    urls = []
    for i in range(1,13):
        url='http://www.mwgif.com/archive/2015/%s' % i
        urls.append(url)
    a = getInfo()
    a.getcontent(urls)
    print "ok"

    urls_reg=r'http:\/\/www\.mwgif\.com\/post\/\d+\/\S+'
    result = a.getmagnet(urls_reg)
    with open(r'url.txt','wb+') as f:
        f.write(str(result))
    return result
def seconed():
    urlslist  = first()
    a = getInfo()
    a.getcontent(urlslist)
    magnet_reg=r'magnet:\?xt=urn:btih:\S+'
    result_magnet = a.getmagnet(magnet_reg)
    with open(r'magnet.txt','wb+') as f:
        f.write(str(result_magnet))
    #print result_magnet
    return result_magnet


if '__name__ = main()':

    urls = seconed()
    print urls
'''
    api = API()
    #touch file ~/.115 format:
    #[default]
    #username = username@example.com
    #password = defaultpassword
    #
    #[another]
    #username = another@example.com
    #password = anotherpassword
    api.login(section='default')
    if  api.has_logged_in:
        print '115已经登陆'
    else:
        print '用户名或密码错误'
    for url in urls:
        api.add_task_url(url)
        time.sleep(5)
    api.logout()
'''
