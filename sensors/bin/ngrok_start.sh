#!/bin/bash
PUBLICIP=`curl icanhazip.com`
echo "ngrok http 80" > /usr/local/bin/startngrok
chmod 755 /usr/local/bin/startngrok
SENSORID=`cat /root/.sensorid`
RESPONSE=`curl -X POST http://192.168.56.101/addsensor/?format=json  -H 'content-type: application/json' -d'
{
    "ip":"'"$PUBLICIP"'",
    "sensorid":"'"$SENSORID"'",
}'`
startngrok
