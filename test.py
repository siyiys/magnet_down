#!/usr/bin/env python
# encoding: utf-8

from getdown import getInfo
a = getInfo()
urls = ['https://fms-sypay-uat.sf-pay.com/index.html','https://fms-sypay-uat.sf-pay.com/index.html']
a.getcontent(urls)
print 'hello'
