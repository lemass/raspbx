#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import os
import urllib2,json
import xml.etree.ElementTree as ET

from flask import Flask,request,make_response,g

error_msg = '哦豁'

app =Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def wxauth():
    if request.method == 'GET':
      data = request.args
      signature = data.get('signature')
      timestamp = data.get('timestamp')
      nonce = data.get('nonce')
      echostr = data.get('echostr')
      token = 'wexin' 
      list=[token,timestamp,nonce]
      list.sort()
      ha1=hashlib.sha1()
      map(sha1.update,list)
      hashcode=sha1.hexdigest()

      if hashcode == signature:
        return make_response(echostr)

    if request.method == 'POST':
      xml_recv = ET.fromstring(request.data)
      ToUserName = xml_recv.find("ToUserName").text
      FromUserName = xml_recv.find("FromUserName").text
      Content = xml_recv.find("Content").text

      reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
      try:
        Content = '测试 自动回复'
        if Content == None : Content = error_msg
      except BaseException:
        Content = error_msg
      response = make_response( reply % (FromUserName, ToUserName, str(int(time.time())), Content ) )
      response.content_type = 'application/xml'
      return make_response(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
