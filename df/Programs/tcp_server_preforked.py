#!/usr/bin/python3
import socket
import os,sys
import time

NUM_CHILDREN = 3
def process_client(ssock):
    pid = os.getpid()
    cnt = 1
    csock, addr = ssock.accept()
    print(f"Child with pid = {pid} accepted conn from {csock}")
    try:
       req = csock.recv(1024)
       print(csock, req.decode())
       csock.send(b"Welcome");
    except Exception as e:
       print("Exception: {}".format(e))
    finally:
       csock.close()

def main():
    if (len(sys.argv) < 2):
       print("Usage: " + sys.argv[0] + " <port number>")
       exit(1)
    port = int(sys.argv[1])
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind(('', port))
    ssock.listen(5)

    for i in range(NUM_CHILDREN):
        pid = os.fork()
        if (pid == 0):  # this is Child process
            process_client(ssock)
            exit(0)
        else:  # This is Parent process
            print("created new client, pid = ", pid)

    for _ in range(NUM_CHILDREN):
        pid, status = os.wait()  
        print(f"[Parent] Child {pid} exited.")

if __name__ == "__main__":
    main()
