#!/usr/bin/env python
# encoding: utf-8
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import time
c = time.strftime("%Y_%m_%d", time.localtime())
#urls = ['https://fms-sypay-uat.sf-pay.com/index.html','https://fms-sypay-uat.sf-pay.com/index.html']
def Getcontent(urls):
    pool = ThreadPool(6)
    result = pool.map(urllib2.urlopen,urls)
    pool.close()
    pool.join()
    f = open("content_%s.txt" % c, 'wb')
    for x in result:
        f.write(x.read())
    f.close()
#Getcontent(urls)
