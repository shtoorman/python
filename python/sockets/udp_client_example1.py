import socket
import codecs

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(1000):
    # a = bytes(i)
    # print(a)
    sock.sendto(b'Test message '+ str(i).encode("utf-8"), ('127.0.0.1', 8888))
sock.close()
