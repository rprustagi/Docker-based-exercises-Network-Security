#!/bin/bash
set -e

if [ ! -f /var/lib/krb5kdc/principal ]; then
    echo "Creating/Initializing Kerberos database..."
    # -s : create stash file which stores encrypted master key
    # 	this helps KDC starts automatically.
    kdb5_util create -s -P masterpassword

    echo "Creating user principals..."
    # two sample users alice, bob are created. Create more users as needed.
    # database information is maintained locally (network not needed)
    kadmin.local -q "addprinc -pw adminpassword admin/admin"
    # for each user create the principal as below
    # kadmin.local -q "addprinc -pw alicepassword alice"

    echo "Creating SSH host principal..."
    # A sample service (ssh server) is created. Add more as needed.
    # services generally use random password, not user typed
    kadmin.local -q "addprinc -randkey host/server.csee.umbc.test"
    kadmin.local -q "addprinc -randkey host/server"
fi

echo "Starting Kerberos KDC..."
krb5kdc

echo "Starting Kerberos admin server..."
#kadmind -nofork
kadmind

