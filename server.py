import socket
import time
# handle the hole message
# 3,000,000,000 = 30 levando em consideração ao 
# protocolo de que deve-se receber até 30 caracteres

HEADERSIZE = 30

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5) ## fila 5

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com o {adress} estabilizada!")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg,"utf-8"))

    while True:
        time.sleep(4)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))