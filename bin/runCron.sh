#!/bin/bash

source /etc/profile

cd $(dirname $0)

./reportClient.py > /dev/null
