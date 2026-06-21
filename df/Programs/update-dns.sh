#!/bin/bash

set -e
if [ $# -eq 0 ]; then
    echo "Usage: ${0} <X>"
    exit 1
fi

X="$1"


X1=$((X + 1))
X2=$((X + 2))
X9=$((X + 9))
X10=$((X + 10))
X11=$((X + 11))

sed \
  -e "s/\<X1\>/${X1}/g" \
  -e "s/\<X2\>/${X2}/g" \
  -e "s/\<X9\>/${X9}/g" \
  -e "s/\<X10\>/${X10}/g" \
  -e "s/\<X11\>/${X11}/g" \
  /etc/bind/db.mynet.local.template > /etc/bind/db.mynet.local
