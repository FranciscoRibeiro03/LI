import socket

hostname = "rui2015.me"
port = 80
location = "/banner_7_824_1.jpg"

def main():
    tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_s.connect( (hostname, port) )

    str_data = "GET " + location + "\n"
    b_data = str_data.encode()
    tcp_s.send(b_data)

    response = b''
    while True:
        b_data = tcp_s.recv(1024)
        response += b_data
        print(len(b_data))
        if len(b_data) < 1024:
            break

    with open('test.jpg', 'wb') as f:
        f.write(response)
    
    tcp_s.close()

main()