import socket
import os
BUFFER_SIZE = 200000
def ReceberArquivo(socket= socket):
        conn, edr = socket.accept()
        try:
            nome = (conn.recv(1024)).decode('UTF-8')
            filename = f'/home/isnan/Trabalho-Redes/Proxy/arquivos/{nome}'
            fileop = open(filename, 'wb')
            fileop.write(conn.recv(BUFFER_SIZE))
            print("Arquivo recebido\n")
            fileop.close()
            data = conn.recv(2048)
            print(data.decode('utf-8'))
            print("passou")
        except:
             print("Não foi possível receber o arquivo!\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5050
HOST = "localhost"
backlog = 1
lista_usuarios = []
lista_endereco = []  
s.bind((HOST,PORT))
s.listen()
ReceberArquivo(s)
#lista_endereco.append(edr)

