#!/bin/bash

ip rule add to 192.168.0.0/16 pref 10000 table 101   
ip route add default via 192.168.3.1 table 101
ip route replace default dev ppp0 table main
