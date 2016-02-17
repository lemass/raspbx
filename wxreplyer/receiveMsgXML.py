#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: wanglin
# Created Time: Fri Jan 29 16:44:28 CST 2016
# File Name: Sample.py
# Description: AppMsgCrypt 使用demo文件
#########################################################################
from AppMsgCrypt import AppMsgCrypt
import xml.etree.cElementTree as ET
import sys
if __name__ == "__main__":
   #app 参数
   sToken = "QDG6eK"
   sEncodingAESKey = "jWmYm7qr5nMoAUwZRjGtBxmz3KA1tkAj3ykkR6q2B2C"
   sAppID = "wx5823bf96d3bd56c7"

   '''
   用户回复的消息解密
   '''
   # sReqMsgSig = HttpUtils.ParseUrl("msg_signature")
   sReqMsgSig = "aa6b4a85c94455f2347b74c405213fa09e5eab12"
   sReqTimeStamp = "1454068008"
   sReqNonce = "20160129"
   sReqData = "<xml><Encrypt><![CDATA[z7iw3PZiKHZ59z8e71xyBnmB63ClkVATJ83Nz4yigwB8616ad5RMqdofh+ChWuq0uy5muaJIG/a4voIS1MtkbaPQQ25gTfPU2SS6gDkG5U+rTqMIfakQE2/A+QdsgVmwjh/jlXGO+Iq5nh37MLjBH2W17YyMlJoDXaLP91tuarNPR/sNYevNLsdtY8jSSWmBQqCyA7jvti6/sZPPS0fEOJXLaMoEYEtdwNvUNuvMdMzUN+oQ7S+EuY1NlLGYMrNCg2kPBdLxNFbZ+LaIVtCb4U4+dw++M6f56VSJiDtMhCJi3ySbsoYKzDau58k2JYUGEtr7P52WuOn9vtxOanZnQA==]]></Encrypt><ToUserName><![CDATA[wanglin]]></ToUserName><MsgSignature><![CDATA[aa6b4a85c94455f2347b74c405213fa09e5eab12]]></MsgSignature><TimeStamp>1454068008</TimeStamp><Nonce><![CDATA[20160129]]></Nonce></xml>"
   appcpt=AppMsgCrypt(sToken,sEncodingAESKey,sAppID)
   ret,sMsg=appcpt.DecryptMsg( sReqData, sReqMsgSig, sReqTimeStamp, sReqNonce)
   print ret
   print sMsg
   if( ret!=0 ):
      print "ERR: DecryptMsg ret: " + str(ret)
      sys.exit(1)
   # 解密成功，sMsg即为xml格式的明文
   # TODO: 对明文的处理
   # For example:
   xml_tree = ET.fromstring(sMsg)
   content = xml_tree.find("Content").text
   print content
