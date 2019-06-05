from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INEТ, SOCK_STREAМ)
tcpCliSock.connect(ADDR)
while True:
    data = raw_input('>')
    if not data:
        break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
            print(data)
            tcpCliSock.close()
