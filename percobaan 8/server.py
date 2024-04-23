import time
import socket
import sys

print("\nWelcome to Chat Room\n")

host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 9900

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(host, "(", ip, ")")
print("Port:", port)
print("Menunggu koneksi")

data_payload = 2048

while True:
    data, address = sock.recvfrom(data_payload)
    if data == b"[e]":
        message = "Keluar Dari Chat Room!"
        sock.sendto(message.encode('utf-8'), address)
        print("\n")
        break
    print("Client %s" % data.decode())
    message = input("Server: ")
    sock.sendto(message.encode('utf-8'), address)

sock.close()