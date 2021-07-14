import socket;

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5) ## fila 5

while True:
    clientsocket, adress = s.accept()
    print(f"Conexão com o {adress} estabilizada!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
'''
