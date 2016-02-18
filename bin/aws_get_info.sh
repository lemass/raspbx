#!/bin/bash

#查看内网IP
curl http://169.254.169.254/latest/meta-data/local-ipv4
echo -ne "\t"

#查看外网IP
curl http://169.254.169.254/latest/meta-data/public-ipv4
echo -ne "\t"

#查看配置
curl http://169.254.169.254/latest/meta-data/instance-type
echo -e "\r"

#查看instance id
curl http://169.254.169.254/latest/meta-data/instance-id
echo -ne "\t"

#查看instance使用的AMI ID
curl http://169.254.169.254/latest/meta-data/ami-id
echo -ne "\t"

#查看instance所在区域
curl http://169.254.169.254/latest/meta-data/placement/availability-zone
echo ""

