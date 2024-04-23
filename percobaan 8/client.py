import time
import socket
import sys
import argparse

data_payload = 2048
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, "(", ip, ")\n")


def menu():
    print("Menu Pilihan:")
    print("1. Koneksi ke server")
    print("2. Melihat history")
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        server_ip = str(input("Masukkan Server Address: "))
        server_port = int(input("Masukkan Port Server: "))
        server = (server_ip, server_port)
        print("Koneksi berhasil")
        print("\nWelcome to Chat Room\n")
        history = open("%s.txt" % server_ip, "a")
        try:
            while True:
                message = str(input("Client: "))
                if message == "Quit" or message == "quit":
                    history.close()
                    print("Data disimpan")
                else:
                    history.write("Client: %s\n" % message)
                    sock.sendto(message.encode('utf-8'), server)
                    data, address = sock.recvfrom(data_payload)
                    if message == "[e]":
                        message = "Keluar Dari Chat Room!"
                        break

                    data = data.decode()
                    print("Server:", data)
                    history.write("Server: %s\n" % data)
        finally:
            print("Closing connection to the server")
            sock.close()
    elif pilihan == 2:
        file = str(input("Masukkan nama file: "))
        history = open("%s.txt" % file, "r")
        print("History Percakapan :")
        print(history.read())

menu()