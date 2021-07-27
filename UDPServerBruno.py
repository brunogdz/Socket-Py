# Aluno: Bruno Gomes de Azevedo
from random import *
from socket import *
from time import sleep
import random 
recieve_host = '127.0.0.1'
recieve_port = 30000


serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((recieve_host, recieve_port))


while True:
  message, address = serverSocket.recvfrom(2048)
  message = message.upper()
  print('Recebido: ' + message.decode())
  numbers = random.randint(0,9)
  msg = '0000%d%dBruno Gomes de Azev' %(numbers,randint(0,1))
  message =  msg.encode("utf-8")
  serverSocket.sendto(message, address)