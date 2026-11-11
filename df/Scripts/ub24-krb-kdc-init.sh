#!/bin/bash
set -e

if [ ! -f /var/lib/krb5kdc/principal ]; then
    echo "Creating/Initializing Kerberos database..."
    # -s : create stash file which stores encrypted master key
    # 	this helps KDC starts automatically.
    kdb5_util create -s -P masterpassword

    echo "Creating user principals..."
    kadmin.local -q "addprinc -pw adminpassword admin/admin"

    # database information is maintained locally (network not needed)
    # create two sample users alice, bob. 
    # Create more users as needed.
    # for each user create the principal as below
    kadmin.local -q "addprinc -pw alicepassword alice"
    kadmin.local -q "addprinc -pw bobpassword bob"

    echo "Creating SSH host principal..."
    # A sample service (ssh server) is created. Add more as needed.
    # services generally use random password, not user typed
    kadmin.local -q "addprinc -randkey host/server1.csee.umbc.test"
    kadmin.local -q "addprinc -randkey host/server1"
    kadmin.local -q "addprinc -randkey host/server2.csee.umbc.test"
    kadmin.local -q "addprinc -randkey host/server2"

    kadmin.local -q "addprinc -randkey host/ws1.csee.umbc.test"
    kadmin.local -q "addprinc -randkey host/ws1"
    kadmin.local -q "addprinc -randkey host/ws2.csee.umbc.test"
    kadmin.local -q "addprinc -randkey host/ws2"
fi

# work as both AS and TGS.
echo "Starting Kerberos KDC: To authenticate and issue tickets...."
krb5kdc

echo "Starting Kerberos admin server..."
# Manages principals etc. used by kinit, kvno, ...
# uses port 88
#kadmind -nofork
kadmind

