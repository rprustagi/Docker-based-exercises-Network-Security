#!/bin/bash
set -e

mkdir -p /run/sshd

useradd -m -s /bin/bash alice || true
echo 'alice:localalice' | chpasswd
mkdir -p /home/alice
echo "alice@CSEE.UMBC.TEST" > /home/alice/.k5login
chown alice:alice /home/alice/.k5login
chmod 600 /home/alice/.k5login

useradd -m -s /bin/bash bob || true
echo 'bob:localbob' | chpasswd
mkdir -p /home/bob
echo "bob@CSEE.UMBC.TEST" > /home/bob/.k5login
chown bob:bob /home/bob/.k5login
chmod 600 /home/bob/.k5login

echo "Waiting for KDC admin server..."
until nc -z kdc.csee.umbc.test 749; do
    sleep 1
done

echo "Installing host keytab..."
rm -f /etc/krb5.keytab

# create a service key for ssh serverL
kadmin -p admin/admin -w adminpassword \
    -q "ktadd -k /etc/krb5.keytab host/server1.csee.umbc.test"
kadmin -p admin/admin -w adminpassword \
    -q "ktadd -k /etc/krb5.keytab host/server1"

chmod 600 /etc/krb5.keytab

echo "Server keytab:"
klist -k -e /etc/krb5.keytab

echo "Starting SSH server..."
#exec /usr/sbin/sshd -D -e
service ssh start
