#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from AppMsgCrypt import AppMsgCrypt,SHA1

#app 参数
sToken = "QDG6eK"

sTimeStamp="1454060148"
sNonce="20160129"
sEchoStr="hello world"

sha1 = SHA1()
ret,signature = sha1.getSHA1(sToken, sTimeStamp, sNonce, sEchoStr)
print signature
if( ret!=0 ):
    print ret

