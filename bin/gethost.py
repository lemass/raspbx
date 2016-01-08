#!/usr/bin/env python
#coding=utf-8

import time
import json
import redis

import os
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_AUTH = os.getenv('REDIS_AUTH')

##initial redis connection
pool = redis.ConnectionPool(host=str(REDIS_HOST), port=int(REDIS_PORT), db=0, password=str(REDIS_AUTH))
r = redis.Redis(connection_pool=pool)

ISOTIMEFORMAT = '%Y-%m-%d %X'
localDate = time.strftime( ISOTIMEFORMAT, time.localtime() )

keys = r.keys("server-*")

res = {}
res['hostSet'] = []
res['date'] = localDate
res['message'] = 'none'
res['total_count'] = len(keys)

for key in keys:
   host = json.loads(r.get(key).replace('\'', '\"'))
   res['hostSet'].append(host)

for i in xrange(len(keys)):
   print res['hostSet'][i]['hostname'] + "\t" + res['hostSet'][i]['ips'][0] + "\t" + res['hostSet'][i]['date']

