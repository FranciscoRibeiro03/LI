import select
import socket

def main():
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_s.bind( ("127.0.0.1", 1234) )

    sock_list = []

    tcp_s.listen()

    while 1:
        socks = select.select([tcp_s, ] + sock_list, [], [])[0]

        for sock in socks:
            if sock == tcp_s:
                client_sock, client_addr = tcp_s.accept()
                if not client_sock in sock_list:
                    sock_list.append(client_sock)
            else:
                b_data = sock.recv(4096)

                for client_sock in sock_list:
                    client_sock.send(b_data)
        
    tcp_s.close()

main()