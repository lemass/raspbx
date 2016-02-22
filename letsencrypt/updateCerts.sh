#!/bin/sh

cd /data/gitbase/raspbx/letsencrypt

for conf in $(ls *.conf); do
  /root/.local/share/letsencrypt/bin/letsencrypt --no-self-upgrade --config "$conf" certonly
done

# make sure nginx picks them up
nginx -s reload
