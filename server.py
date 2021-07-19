import socket
import time
import pickle



# handle the hole message
# 3,000,000,000 = 30 levando em consideração ao 
# protocolo de que deve-se receber até 30 caracteres

HEADERSIZE = 30

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5) ## fila 5

while True:
    clientsocket, address = s.accept()
    print(f"Conexão com o {address} estabilizada!")

    d = {1: "ping", 2: "pong"}
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

    clientsocket.send(msg)

    # while True:
    #     time.sleep(4)
    #     msg = f"The time is {time.time()}"
    #     msg = f"{len(msg):<{HEADERSIZE}}"+msg

    #     print(msg)

    #     clientsocket.send(bytes(msg,"utf-8"))
        
