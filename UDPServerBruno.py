# Aluno: Bruno Gomes de Azevedo

from socket import *
from time import sleep

recieve_host = '127.0.0.1'
recieve_port = 30000


serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((recieve_host, recieve_port))


while True:
  message, address = serverSocket.recvfrom(2048)
  message = message.upper()
  print('Recebido: ' + message.decode())
  msg = '0001'
  message =  msg.encode("utf-8")
  serverSocket.sendto(message, address)