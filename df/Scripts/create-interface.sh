#!/bin/bash
# Run this program on Linux VM, and not inside any container.

#---------------------------------------------
# Function to connect two containers with a veth pair
# input parameters
# $1 - container name
# $2 - container interface
# $3 - container connected to
# $4 - interface of connected container.
#
connect_veth() {
    cntnr=$1
    if_cntnr=$2
    other_cntnr=$3
    if_other_cntnr=$4

    pid_cntnr=$(docker inspect -f '{{.State.Pid}}' ${cntnr})
    pid_other_cntnr=$(docker inspect -f '{{.State.Pid}}' ${other_cntnr})

    # Create veth pair (basically create a virtual ethernet cable)
    sudo ip link add ${if_cntnr} type veth peer name ${if_other_cntnr}

    # Move into namespaces
    sudo ip link set ${if_cntnr} netns $pid_cntnr
    sudo ip link set ${if_other_cntnr} netns $pid_other_cntnr

    # Bring up inside containers
    sudo nsenter -t $pid_cntnr -n ip link set ${if_cntnr} up
    sudo nsenter -t $pid_other_cntnr -n ip link set ${if_other_cntnr} up
}
#---------------------------------------------
if [ $# -lt 4 ]; then
  echo "Usage: $0 <sys1> <if-sys1> <sys2> <if-sys2>"
  exit 1
fi
sys1="$1"
if-sys1="$2"
sys2="$3"
if-sys3="$4"

echo "[*] Wiring containers with veth pairs..."
set -ex

# Connect sys1 -- sys2
connect_veth ${sys1} ${if-sys1} ${sys2} ${if-sys2}
