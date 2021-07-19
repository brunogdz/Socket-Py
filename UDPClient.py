import socket
client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
i = 0
msg = "ping"
for i in range(10):
    client_sock.sendto(msg.encode("utf-8"),('127.0.0.1',12345))
    data,fl,addr=client_sock.recvfrom(4096)
    print(str(data))
    client_sock.close()