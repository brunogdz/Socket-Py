import socket
import time


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))
sock.listen(5)


start = time()
timeout = 5
while True:
    data,addr=sock.recvfrom(4096)
    print(str(data))
    msg = "ping"
    msg = bytes(f"{len(msg):<30}", "utf-8") + msg
    sock.sendto(msg,1,addr)