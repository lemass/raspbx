#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from AppMsgCrypt import AppMsgCrypt,SHA1

#app 参数
sToken = "QDG6eK"
sEncodingAESKey = "jWmYm7qr5nMoAUwZRjGtBxmz3KA1tkAj3ykkR6q2B2C"
sAppID = "wx5823bf96d3bd56c7"
appcpt=AppMsgCrypt(sToken,sEncodingAESKey,sAppID)

sTimeStamp="1454060148"
sNonce="20160129"
sEchoStr="hello world"
tousername='wanglin'

sha1 = SHA1()
ret,signature = sha1.getSHA1(sToken, sTimeStamp, sNonce, sEchoStr)
print signature
if( ret!=0 ):
    print ret

# xml消息模板   
AES_TEXT_RESPONSE_TEMPLATE = """<xml><Content><![CDATA[%(Content)s]]></Content><TimeStamp><![CDATA[%(TimeStamp)s]]></TimeStamp><ToUserName><![CDATA[%(ToUserName)s]]></ToUserName><signature><![CDATA[%(signature)s]]></signature></xml>"""

encrypt = '你好'

resp_dict = {
    'ToUserName': tousername,
    'Content' : encrypt,
    'TimeStamp' : sTimeStamp,
    'signature' : signature,
}
resp_xml = AES_TEXT_RESPONSE_TEMPLATE % resp_dict
print resp_xml

ret,sEncryptMsg=appcpt.EncryptMsg(resp_xml, sNonce)
print sEncryptMsg
if( ret!=0 ):
    print "ERR: EncryptMsg ret: " + ret
    sys.exit(1)
