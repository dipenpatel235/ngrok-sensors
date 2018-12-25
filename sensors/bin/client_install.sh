#!/bin/bash
PUBLICIP=`curl icanhazip.com`
RESPONSE=`curl -X POST http://192.168.56.101/addsensor/?format=json  -H 'content-type: application/json' -d'
{
    "ip":"'"$PUBLICIP"'"
}'`
apt-get install jq
NGROKID=`echo "$RESPONSE" | jq -r '.ngrokid'`
SENSORID=`echo "$RESPONSE" | jq -r '.token'`
echo "$SENSORID" > /root/.sensorid
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
./ngrok authtoken $NGROKID
mv ngrok /usr/local/bin/

echo "Successfully Installation done"