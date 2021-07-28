# Aluno: Bruno Gomes de Azevedo


import time
import sys
import socket

host = "127.0.0.1" #set to server ip or hostname
port = 30000

pings = 10
timeout = 5
sleep_time = 1
message_bytes = 30
mensagemErro = 0
min_ping = 999999
max_ping = 0
ping_count = 0
ping_received = 0
avg_ping = 0

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(timeout)

def checkMessage(mes):
    if(mes != '1'):
        return True


def verificaCampos(str,host,vFinal):
    if len(str) < 30:
        # print('O teste é esse' + str)
        checkOrdem = str[:5]
        checkPong = str[5]
        var = int(checkOrdem)
        if var >= 0 and var <= 9:
            if checkPong == '1':      
                print('recebido %s from %s requisicao=%d time=%0.1f ms' % (str, host, var, vFinal))
            else: 
                return True
        # print(checkOrdem)
        else:
            return True
    else:
        return True

def data_error(seq):
    print("No %dª envio, o servidor respondeu algo que nao foi reconhecido nos nossos padroes do protocolo" %(seq))

def show_summary():
    total_time = (time.time() - time_start) * 1000

    print('---  Ping e Pong com o servidor %s ---' % (host))
    print('%d packets transmitted, %d received, %0.0f%% packet loss, time %0.0fms' % (pings, ping_received, (pings - ping_received) / pings * 100, total_time))
    print('rtt min/avg/max/mdev = %0.3f/%0.3f/%0.3f/%0.3f ms' % (min_ping, avg_ping / ping_count, max_ping, max_ping - min_ping))
    sys.exit()

time_start = time.time()
packetLoss = 0

for seq in range(pings):
    try:
        
        start = time.time()
        msg = '0000%d' %seq
        timestamp = str(int((start-time_start)*1000)).zfill(4)
        msgf = '%s0%sBrunoGomesdeAzevedo' %(msg,timestamp[:4])
        msg_up = msgf[:message_bytes]
        message =  msg_up.encode("utf-8")
        clientSocket.sendto(message, (host, port))
        data, server = clientSocket.recvfrom(2048)
        end = time.time()
        vFinal = (end - start) * 1000
        if vFinal < min_ping: min_ping = vFinal
        if vFinal > max_ping: max_ping = vFinal
        ping_count += 1
        ping_received += 1
        avg_ping += vFinal

        # print('recebido %s from %s time=%0.1f ms' % (data.decode(), host, vFinal))
        time.sleep(sleep_time)
        #teste = data.decode()[5]
        teste = data.decode()
        # check = checkMessage(teste)
        check = verificaCampos(teste,host,vFinal)
        if(check == True):
            mensagemErro += 1
            ping_received = ping_received - 1
            #ping_received = ping_received - 1
    except socket.timeout as error:
        print('Dado = %d REQUEST TIMED OUT' % (seq))
        
    except KeyboardInterrupt:
        show_summary()
print('Houve %d fora do padrão do protocolo' %(mensagemErro))
show_summary()
