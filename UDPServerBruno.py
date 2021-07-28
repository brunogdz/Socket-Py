# # Aluno: Bruno Gomes de Azevedo
# from random import *
# from socket import *
# from time import sleep
# import random 
# recieve_host = '127.0.0.1'
# recieve_port = 30000


# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind((recieve_host, recieve_port))


# while True:
#   message, address = serverSocket.recvfrom(2048)
#   message = message.upper()
#   print('Recebido: ' + message.decode())
#   numbers = random.randint(0,9)
#   msg = '0000%d%dBruno Gomes de Azev' %(numbers,randint(0,1))
#   message =  msg.encode("utf-8")
#   serverSocket.sendto(message, address)
from socket import *
import random
from time import sleep

# What's your IP address and witch port should we use?
recieve_host = '127.0.0.1'
recieve_port = 30000

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((recieve_host, recieve_port))

while True:

    rand = random.randint(0, 20)

    message, address = serverSocket.recvfrom(1024)

    # message = message.upper()

    print(b'RECEBIDO = ' + message)

    if rand == 2 or rand == 0:
        continue

    message = message.decode("utf-8")

    message = list(message)

    if rand == 1:
        message[0:4] = "00101"
    if rand == 3:
        message[10:] = "Magnos Martinello"
    if rand == 5:
        message[5] = "a"
    else:
        message[5] = "1"

    message = "".join(message)

    message = message.encode("utf-8")

    print(b'ENVIADO = ' + message)

    serverSocket.sendto(message, address)