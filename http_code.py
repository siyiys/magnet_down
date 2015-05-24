#!/usr/bin/env python
# encoding: utf-8

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(6)
urls = []
for i in range(1,13):
      print  i
      url='http://www.mwgif.com/archive/2015/%s' % i
      urls.append(url)
try:
    result = pool.map(urllib2.urlopen,urls)
    pool.close()
    pool.join()
    for x in result:
        print  x.read()
except urllib2.URLError, e:
    print e.reason
except urllib2.HTTPError, e:
        print e.code
else:
    print 'ok'
#finally:
#    print "this a finally"

