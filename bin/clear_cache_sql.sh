#!/bin/bash

[ -f /etc/init.d/functions ] && . /etc/init.d/functions
[ -f /lib/lsb/init-functions ] && . /lib/lsb/init-functions

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
