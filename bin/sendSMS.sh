#!/bin/bash

curl -i -d "secret=xxx" -d "mobi=phone1,phone2" -d "msg=test8"  http://freeapi.picp.net/sms/send.php
