#!/usr/bin/env python
# encoding: utf-8
import re
import time
c = time.strftime("%Y_%m_%d", time.localtime())
regs=r'www\.mwgif\.com\/post\/\d+\/\S+'


def getmagnet(regs):
        pattern = re.compile(regs)
        listcontent = []
        with open(r"content_%s.txt" % c,'r') as f :
                content = f.read()
                result = pattern.findall(content)
                for x in result:
                    listcontent.append(x.split('"')[0])
        return listcontent



