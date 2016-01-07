#!/usr/bin/env python
#coding=utf-8

import time
import json
import redis
import socket
import fcntl
import struct

import os
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_AUTH = os.getenv('REDIS_AUTH')

## get local ip address
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


##initial redis connection
pool = redis.ConnectionPool(host=str(REDIS_HOST), port=int(REDIS_PORT), db=0, password=str(REDIS_AUTH))
r = redis.Redis(connection_pool=pool)

## report my info
def report_hosts():
    localIP = get_ip_address('eth0')
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    localDate = time.strftime( ISOTIMEFORMAT, time.localtime() )
    data = {'hostSet':[{'name':'raspbx', 'ip':localIP, 'date':localDate},{'name':'duck', 'ip':'192.168.2.36', 'date':'2016-01-07 18:43:11'}],'totalCount': 2,'message':'none'}
    sethosts = r.set('host',data)
    gethosts = r.get('host')
    return gethosts

result = report_hosts()
result = str(result).replace('\'', '\"')

res = json.loads(result)
print res['hostSet'][0]
print res['hostSet'][1]

