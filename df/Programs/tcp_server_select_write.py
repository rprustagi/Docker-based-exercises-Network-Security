#!/usr/bin/env python3
"""
TCP echo-style server using select() with a per-send cap of 1000 bytes.

Behavior:
- Accepts multiple clients.
- Reads up to 1000 bytes at a time from a readable client socket.
- Queues the response in a per-socket write buffer.
- On each writable event, attempts to send at most 1000 bytes.
- Removes sockets cleanly from all tracking structures on close/error.
"""

import sys
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_SNDBUF, SO_RCVBUF, socket
from select import select

MAX_RW_CHUNK = 1000
TIMEOUT = 10


def close_client(sock, csocks, wsocks, wmsgs):
    """Remove a client socket from all tracking structures and close it."""
    try:
        try:
            peer = sock.getpeername()
            print("Closing:", peer)
        except OSError:
            print("Closing a client socket")

        if sock in wsocks:
            wsocks.remove(sock)
        if sock in csocks:
            csocks.remove(sock)
        wmsgs.pop(sock, None)
        sock.close()
    except OSError:
        pass


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <server IP> <port number>")
        sys.exit(1)

    ipaddr = sys.argv[1]
    port = int(sys.argv[2])

    lsock = socket(AF_INET, SOCK_STREAM)
    lsock.setsockopt(SOL_SOCKET, SO_SNDBUF, 4096)
    lsock.setsockopt(SOL_SOCKET, SO_RCVBUF, 4096)
    lsock.bind((ipaddr, port))
    lsock.listen(5)
    lsock.setblocking(False)

    # connected client sockets
    csocks = []

    # sockets that currently have pending outbound data
    wsocks = []

    # per-socket pending outbound bytes
    wmsgs = {}

    print(f"Listening on {ipaddr}:{port}")

    while True:
        try:
            rl, wl, el = select([lsock] + csocks, wsocks, csocks, TIMEOUT)
        except OSError as exc:
            print("select() failed:", exc)
            break

        if not (rl or wl or el):
            print(f"select() call timed out for {TIMEOUT} seconds")
            continue

        # Handle socket errors first.
        for esock in list(el):
            close_client(esock, csocks, wsocks, wmsgs)

        # Handle readable sockets.
        for rsock in list(rl):
            if rsock is lsock:
                try:
                    nsock, cliaddr = lsock.accept()
                    nsock.setblocking(False)
                    csocks.append(nsock)
                    wmsgs[nsock] = b""
                    print("Received new connection from", cliaddr)
                except OSError as exc:
                    print("accept() failed:", exc)
                continue

            try:
                rmsg = rsock.recv(MAX_RW_CHUNK)
            except OSError:
                close_client(rsock, csocks, wsocks, wmsgs)
                continue

            # recv() returning b"" means peer closed gracefully.
            if not rmsg:
                try:
                    print("Peer closed:", rsock.getpeername())
                except OSError:
                    print("Peer closed")
                close_client(rsock, csocks, wsocks, wmsgs)
                continue

            try:
                decoded = rmsg.decode("ascii")
            except UnicodeDecodeError:
                decoded = rmsg.decode("ascii", errors="replace")

            print("Rcvd from:", rsock.getpeername(), ", data:", decoded)
            decoded += "A"*1000 + "B"*1000 

            if decoded.lower().strip() == "exit":
                close_client(rsock, csocks, wsocks, wmsgs)
                continue

            myip = rsock.getsockname()[0]
            smsg = f"{myip}: {decoded.upper()}".encode("ascii", errors="replace")

            # Append to this socket's write buffer.
            wmsgs[rsock] = wmsgs.get(rsock, b"") + smsg
            if rsock not in wsocks:
                wsocks.append(rsock)

        # Handle writable sockets.
        for wsock in list(wl):
            out = wmsgs.get(wsock, b"")

            if out:
                try:
                    # Attempt to send at most 1000 bytes in this send() call.
                    sentlen = wsock.send(out[:MAX_RW_CHUNK])
                    print(f"Sent {sentlen} bytes to {wsock.getpeername()}")
                except OSError:
                    close_client(wsock, csocks, wsocks, wmsgs)
                    continue

                # Remove only the bytes that were actually sent.
                wmsgs[wsock] = out[sentlen:]

            # If nothing remains queued, stop monitoring for writability.
            if not wmsgs.get(wsock, b""):
                if wsock in wsocks:
                    wsocks.remove(wsock)

    for csock in list(csocks):
        close_client(csock, csocks, wsocks, wmsgs)
    lsock.close()


if __name__ == "__main__":
    main()
