import socket
from threading import Thread

BUFFER_SIZE = 200000

def start(porta = int, host = str ):
    
    PORT = porta
    HOST = host
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST,PORT))
    except:
        return print("Falha na conexão")
    print("Conectado em:" , HOST)
    #Thread(target=ReceberArquivo(s, input("Nome do arquivo:\n"))).start()
    Thread(target=EnviarArquivoProxy(input("Nome do usuario:\n"),input("Nome do arquivo:\n"),input("Tolerancia:\n"),s)).start()
    

def EnviarArquivoProxy(username = str ,arquivo = str, nvl_tol = str, socket = socket):
  #while True:  
    try:
        socket.send(str.encode(arquivo))
        filename = f'/home/isnan/Trabalho-Redes/Clientes/enviar/{arquivo}'
        fileop = open(filename, "rb")
        file = fileop.read(200000)
        socket.sendall(file) #arquivo
        socket.send(str.encode(nvl_tol))#replicas
        print(nvl_tol)
        fileop.close()
    except:
        print("Não foi possível enviar arquivo!\n")
        #break
def EnviarArquivo(socket = socket , dir = str, tamanho = int, nvl_tol = int ):
    filename = dir
    fileop = open(filename, 'rb')
    file = fileop.read(tamanho)
    socket.sendall(file)
    print("Arquivo enviado")
    fileop.close()

def ReceberArquivo(socket= socket, nome = str):
  while True:  
    try:
        filename = f'/home/isnan/Trabalho-Redes/Clientes/recebidos/{nome}'
        fileop = open(filename, 'wb')
        fileop.write(socket.recv(BUFFER_SIZE))
        print("Arquivo recebido")
        fileop.close()
    except:
        print("Não foi possível receber arquivo!\n")
        break

start(5050, "localhost")

 
