#!/bin/bash

# run websocket chat server in the background
python3 Programs/chat_websocket_server.py &

# Run Apache in the foreground to keep container alive
service apache2 start
tail -f /dev/null
