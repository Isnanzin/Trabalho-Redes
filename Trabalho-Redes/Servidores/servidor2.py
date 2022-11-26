import socket #socket: combinação de ip com número de porta

HOST = "" #endereço ip da maquina
PORT = 5050        #porta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); #criação do socket (IPV4, TCP) - serviço de rede/ serviço de transporte

s.bind((HOST, PORT)) #vinculando HOST e PORTA com nosso socket
s.listen() #esperando conexão com o cliente
print("aguardando conexão \n")
conn, endr = s.accept()
filename = "/home/isnan/Trabalho-Redes/Servidores/foto.jpeg" #arquivo a enviar
fileop = open(filename, 'rb')  #abrindo em modo leitura
file = fileop.read(200000)  #abrindo lendo e alocando no file
conn.sendall(file) #enviando tudo
conn.close() #fecha conex
fileop.close() # fecha conex

