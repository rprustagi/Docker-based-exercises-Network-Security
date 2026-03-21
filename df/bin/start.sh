#!/bin/bash

# run websocket chat server in the background
python3 Programs/demo-ws.py &

# Run Apache in the foreground to keep container alive
service apache2 start
tail -f /dev/null
