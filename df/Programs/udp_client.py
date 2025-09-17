#!/usr/bin/env python3
import socket
import time
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple Server for N/w Delays")
parser.add_argument('-s', '--server', type=str, required=True)
parser.add_argument('-p', '--port', type=int, required=True)
parser.add_argument('-c', '--count', type=int, default=10)
parser.add_argument('-d', '--delay', type=float, default=5.0)
parser.add_argument('-b', '--buffer', type=int, default=20)
args = parser.parse_args()

ip_addr = args.server
port = args.port
count = args.count
delay = args.delay
buffer = args.buffer

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvr_addr = (ip_addr, port)

for i in range(count):
    msg = chr(64 + i) * buffer
    current_time = datetime.now().time()
    print (current_time.strftime("%H:%M:%S.%f")[:-3] + " " +"sending: " + msg)
    sent = sock.sendto(msg.encode(), srvr_addr)
    time.sleep(delay)

