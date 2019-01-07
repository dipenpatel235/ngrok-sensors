#!/bin/bash
usage(){
	echo "Usage: $0 sensorid"
	exit 1
}

[[ $# -ne 1 ]] && usage

apt-get install jq
PUBLICIP=`curl icanhazip.com`
SENSOR_ID="$1"


RESPONSE=`curl -X GET "http://192.168.56.101/installsensor/?sensorid=$SENSOR_ID&ip=$PUBLICIP"`
echo $RESPONSE

NGROKID=`echo "$RESPONSE" | jq -r '.ngrokid'`
SENSORID=`echo "$RESPONSE" | jq -r '.sensorid'`


if [ "$SENSORID" == "$SENSOR_ID" ]; then
    echo "$SENSORID" > /root/.sensorid
    wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    unzip ngrok-stable-linux-amd64.zip
    ./ngrok authtoken $NGROKID
    mv ngrok /usr/local/bin/
    wget https://raw.githubusercontent.com/dipenpatel235/ngrok-sensors/master/sensors/bin/ngrok_start.sh -O /usr/local/bin/ngrok_start
    chmod 777 /usr/local/bin/ngrok_start    
    ngrok_start
    echo "Successfully Installation done. You can start service by startngrok command"
else 
    echo "Sensor Id is not matched with our data. please contact system admin."
fi
