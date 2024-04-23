import time
import socket
import sys
import argparse
import os

data_payload = 2048
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, "(", ip, ")\n")


def menu():
    print("Menu Pilihan:")
    print("1. Koneksi ke server")
    print("2. Melihat history")
    print("3. Hapus history")
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        connect_to_server()
    elif pilihan == 2:
        file = str(input("Masukkan nama file: "))
        history_file = f"{file}.txt"
        with open(history_file, "r") as history:
            print("History Percakapan:")
            print(history.read())
    elif pilihan == 3:
        file = str(input("Masukkan nama file yang ingin dihapus: "))
        history_file = f"{file}.txt"
        try:
            os.remove(history_file)
            print("History file berhasil dihapus.")
        except FileNotFoundError:
            print("File tidak ditemukan.")


def connect_to_server():
    server_ip = str(input("Masukkan Server Address: "))
    server_port = int(input("Masukkan Port Server: "))
    server = (server_ip, server_port)
    sock.connect(server)
    print("Koneksi berhasil")
    print("\nWelcome to Chat Room\n")
    history_file = f"{server_ip}.txt"
    history = open(history_file, "a")
    try:
        while True:
            message = str(input("Client: "))
            if message in {"Quit", "quit"}:
                history.close()
                print("Data disimpan")
                break
            else:
                history.write("Client: %s\n" % message)
                sock.sendall(message.encode('utf-8'))
                data = sock.recv(data_payload)
                if message == "[e]":
                    message = "Keluar Dari Chat Room!"
                    break

                data = data.decode()
                print("Server:", data)
                history.write("Server: %s\n" % data)
    finally:
        print("Closing connection to the server")
        sock.close()


menu()


class ChatClient:
    def _init_(self):
        self.data_payload = 2048
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.history_file = None

    def print_host_info(self):
        print(self.host, "(", self.ip, ")\n")

    def show_menu(self):
        print("Menu Pilihan:")
        print("1. Koneksi ke server")
        print("2. Melihat history")
        print("3. Hapus history")
        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            self.connect_to_server()
        elif pilihan == 2:
            file = str(input("Masukkan nama file: "))
            self.history_file = f"{file}.txt"
            with open(self.history_file, "r") as history:
                print("History Percakapan:")
                print(history.read())
        elif pilihan == 3:
            file = str(input("Masukkan nama file yang ingin dihapus: "))
            self.history_file = f"{file}.txt"
            try:
                os.remove(self.history_file)
                print("History file berhasil dihapus.")
            except FileNotFoundError:
                print("File tidak ditemukan.")

    def connect_to_server(self):
        server_ip = str(input("Masukkan Server Address: "))
        server_port = int(input("Masukkan Port Server: "))
        server = (server_ip, server_port)
        self.sock.connect(server)
        print("Koneksi berhasil")
        print("\nWelcome to Chat Room\n")
        self.history_file = f"{server_ip}.txt"
        history = open(self.history_file, "a")
        try:
            while True:
                message = str(input("Client: "))
                if message in {"Quit", "quit"}:
                    history.close()
                    print("Data disimpan")
                    break
                else:
                    history.write("Client: %s\n" % message)
                    self.sock.sendall(message.encode('utf-8'))
                    data = self.sock.recv(self.data_payload)
                    if message == "[e]":
                        message = "Keluar Dari Chat Room!"
                        break

                    data = data.decode()
                    print("Server:", data)
                    history.write("Server: %s\n" % data)
        finally:
            print("Closing connection to the server")
            self.sock.close()


chat_client = ChatClient()
chat_client.print_host_info()
chat_client.show_menu()