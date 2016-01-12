#!/bin/bash

cat << EOF > /etc/apt/sources.list
deb http://mirrors.opencas.cn/raspbian/raspbian/ jessie main
deb-src http://mirrors.opencas.cn/raspbian/raspbian/ jessie main
EOF
