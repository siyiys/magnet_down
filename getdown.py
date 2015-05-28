#!/usr/bin/env python
# encoding: utf-8
import re
import urllib2
import time
from multiprocessing.dummy import Pool as ThreadPool
class getInfo:

    c = time.strftime("%Y_%m_%d", time.localtime())
    """docstring for GetInfo"""
    def __init__(self):
        self.c = time.strftime("%Y_%m_%d", time.localtime())
    def getcontent(self,urls):
        pool = ThreadPool(6)
        result = pool.map(urllib2.urlopen,urls)
        pool.close()
        pool.join()
        f = open("content_%s.txt" % self.c, 'wb')
        for x in result:
            f.write(x.read())
        f.close()
    def getmagnet(regs):
        pattern = re.compile(regs)
        listcontent = []
        with open(r"content_%s.txt" % c,'r') as f :
                content = f.read()
                result = pattern.findall(content)
                for x in result:
                    listcontent.append(x.split('"')[0])
        return listcontent
