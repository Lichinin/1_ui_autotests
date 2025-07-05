#!/bin/bash

SELENIUM_SERVER="./selenium-server"
HUB_PORT=4444
NODE_COUNT=2
HOST="127.0.0.1"

echo "Starting Hub on port $HUB_PORT"
java -jar "$SELENIUM_SERVER" hub --port $HUB_PORT --host $HOST &

sleep 5

for ((i=1; i<=NODE_COUNT; i++))
do
    PORT=$((5550 + i))
    echo "Starting Node $i on port $PORT"
    java -jar "$SELENIUM_SERVER" node --port $PORT --hub "http://$HOST:$HUB_PORT" --host $HOST &
done

echo -e "\nGrid started: http://localhost:$HUB_PORT/grid/console"