#!/usr/bin/env python
#coding=utf-8

import time
import json
import redis

import os
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_AUTH = os.getenv('REDIS_AUTH')

## get local ip address
import socket
import fcntl
import struct
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

## get mac address
import uuid
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return "server-" + mac
    #return ":".join([mac[e:e+2] for e in range(0,11,2)])

##initial redis connection
pool = redis.ConnectionPool(host=str(REDIS_HOST), port=int(REDIS_PORT), db=0, password=str(REDIS_AUTH))
r = redis.Redis(connection_pool=pool)

## report my info
ISOTIMEFORMAT = '%Y-%m-%d %X'
localDate = time.strftime( ISOTIMEFORMAT, time.localtime() )
localName = socket.gethostname()

eth = sorted(os.listdir('/sys/class/net/'))
localIP = []
if len(eth) > 2:
    localIP.append(get_ip_address(eth[1]))
    localIP.append(get_ip_address(eth[0]))
else:
    localIP.append(get_ip_address(eth[0]))

host = {'hostname':localName, 'ips': localIP, 'date':localDate}
r.set(get_mac_address(),host)
