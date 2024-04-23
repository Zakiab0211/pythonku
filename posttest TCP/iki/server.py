import socket
import sys

print("\nWelcome to Chat Room\n")

host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print(host, "(", ip, ")")
print("Port:", port)
print("Menunggu koneksi")

data_payload = 2048


def send_message(client_socket, message):
    client_socket.sendall(message.encode('utf-8'))


def receive_message(client_socket):
    data = client_socket.recv(data_payload)
    return data.decode()


while True:
    client_socket, address = sock.accept()
    print("Terhubung dengan client", address)

    while True:
        data = receive_message(client_socket)
        if data == "[e]":
            message = "Keluar Dari Chat Room!"
            send_message(client_socket, message)
            print("\n")
            break
        print(f"Client {data}")
        message = input("Server: ")
        send_message(client_socket, message)

    client_socket.close()
    print("Closing connection to the client")

sock.close()