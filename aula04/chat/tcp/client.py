import select
import socket
import sys

def main():
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_s.connect( ('127.0.0.1', 1234) )

    while 1:
        rsocks = select.select([tcp_s, sys.stdin, ], [], [])[0]

        for sock in rsocks:
            if sock == tcp_s:
                b_data = tcp_s.recv(4096)
                sys.stdout.write("%s\n" % b_data.decode("utf-8"))
            elif sock == sys.stdin:
                str_data = sys.stdin.readline()
                tcp_s.send(str_data.encode("utf-8"))

    tcp_s.close()

main()