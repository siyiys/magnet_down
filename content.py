#!/usr/bin/env python
# encoding: utf-8

from getdown import getInfo

def first():
    i = 1
    for i in range(10):
        urls= 'xxx/%s '
        a = getInfo()
        a.getcontent(urls)

    urls_reg=r'www\.mwgif\.com\/post\/\d+\/\S+'
    result = a.getmagnet(urls_reg)
    return result

def seconed():
    urlslist  = first()
    a = getInfo()
    a.getcontent(urlslist)
    magnet_reg=r'magnet:\?xt=urn:btih:\S+'
    result_magnet = a.getmagnet(magnet_reg)
    return result_magnet
