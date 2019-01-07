#!/bin/bash
PUBLICIP=`curl icanhazip.com`
echo "ngrok http 80" > /usr/local/bin/startngrok
chmod 755 /usr/local/bin/startngrok
