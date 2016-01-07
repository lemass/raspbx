#!/usr/bin/env python
#coding=utf-8

import redis
import socket
import fcntl
import struct

## get local ip address
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


##initial redis connection
pool = redis.ConnectionPool(host='54.169.181.13', port=6301, db=0, password='8Nt7omthtJXGsXep')
r = redis.Redis(connection_pool=pool)

## report my info
localIP = get_ip_address('eth0')
r.set('ping',localIP)

#res = r.get('ping')
#print res

