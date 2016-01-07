#!/bin/bash
#By Chenxin 20120717

if [ -f /etc/init.d/functions ];then
. /etc/init.d/functions;
fi

PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

sync
sync
echo 1 > /proc/sys/vm/drop_caches 
sleep 2;
sync
sleep 2;
echo 2 > /proc/sys/vm/drop_caches  
sleep 2;
sync
sleep 2;
echo 3 > /proc/sys/vm/drop_caches  
sleep 2;
sync
sleep 2;
sync
