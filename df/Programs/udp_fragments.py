#!/usr/bin/env python3
# this program simply spoofs a UDP with fragmentation
# -------------------------------
import sys
from scapy.all import *
import time
import random

if len(sys.argv) != 6:
  print("Usage: sys.argv[0] <src ip> <src port> <dst IP> <dst port> <num fragments>")
  exit()

srcip = sys.argv[1]
srcport = int(sys.argv[2])
dstip = sys.argv[3]
dstport = int(sys.argv[4])
num_frags = int(sys.argv[5])

flen = [None] * num_frags
payload = [None] * num_frags
offset = [None] * num_frags
pktfrag = [None] * num_frags

fragID = random.randint(1000,60000)

for i in range(num_frags):
  flen[i] = random.randint(2,10) * 8
	payload[i] = chr(ord('A')+i) * (flen[i] - 1) + "\n"

next_offset = 0


udp = UDP(sport = srcport, dport=dstport, chksum=0)
# preparing fragments
for i in range(num_frags):
  fragment_offset = next_offset // 8
  fragment_data = Raw(load=payload[i])

  next_offset += len(payload[i])

	if i == 0:
    fragment_data = udp / Raw(load=payload[i])
		next_offset += 8 

	more_frags = 1 < num_frags - 1
	flagbits = "MF" if more_fragments else 0

  ip = IP(src=srcip,  
	        dst=dstip, 
					id=fragID, 
					frag=fragment_ofset, 
					flags=flagbits, 
          ip.proto = 17,
				)
	pktfrag[i] = ip / fragment_data

# fragment construction over. start sending these fragments
frag_seq = [i for i in range(num_frags)]
random.shuffle(frag_seq)

for i in range(num_frags):
  curr_frag = frag_seq.pop()
  print(f"sending Fragment {curr_frag}")
  send(pktfrag[curr_frag])
  delay = random.randint(2,10)
  print(f"sending next Fragment after {delay}s")
  time.sleep(delay)

