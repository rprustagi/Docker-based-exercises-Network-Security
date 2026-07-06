#!/bin/bash

named-checkconf
named-checkzone mynet.local /etc/bind/db.mynet.local

echo "Starting DNS server for mynet.local with X=$X"

named -g -u bind
