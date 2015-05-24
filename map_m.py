#!/usr/bin/env python
# encoding: utf-8
import urllib2
urls = ['http://www.baidu.com/','http://segmentfault.com/a/1190000000414339','http://www.126.com']
results = map(urllib2.urlopen,urls)
print results
