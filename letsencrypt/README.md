Nginx with letsencrypt
======================

1.获取客户端

	git clone https://github.com/letsencrypt/letsencrypt /usr/local/letsencrypt

2.添加域名到配置文件

	$ cat /data/gitbase/raspbx/letsencrypt/api.dbca.cn.conf
	domains = api.dbca.cn
	
	# increase key size
	rsa-key-size = 4096
	
	# the current closed beta (as of 2015-Nov-07) is using this server
	server = https://acme-v01.api.letsencrypt.org/directory
	
	# this address will receive renewal reminders, IIRC
	email = wanglin@dbca.cn
	
	# turn off the ncurses UI, we want this to be run as a cronjob
	text = True
	
	# authenticate by placing a file in the webroot (under .well-known/acme-challenge/) and then letting
	# LE fetch it
	authenticator = webroot
	webroot-path = /data/webroot/

3.修改nginx配置，以申请证书时验证域名控制权

4.获取证书

	/usr/local/letsencrypt/letsencrypt-auto --config /data/gitbase/raspbx/letsencrypt/api.dbca.cn.conf certonly

生成的证书在：

	/etc/letsencrypt/live/api.dbca.cn/

5.修改ngxin配置，添加ssl证书

        listen 443 ssl;
        ssl on;
        ssl_certificate /etc/letsencrypt/live/api.dbca.cn/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/api.dbca.cn/privkey.pem;

6.重新加载nginx

	nginx -t & nginx -s reload

7.自动更新证书脚本

	# cat /data/gitbase/raspbx/letsencrypt/updateCerts.sh
	#!/bin/sh
	
	cd /data/gitbase/raspbx/letsencrypt
	
	for conf in $(ls *.conf); do
	  /root/.local/share/letsencrypt/bin/letsencrypt --no-self-upgrade --config "$conf" certonly
	done
	
	# make sure nginx picks them up
	nginx -s reload
	
