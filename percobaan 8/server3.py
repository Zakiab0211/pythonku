import socket

print("\nWelcome to Chat Room\n")

host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(host, "(", ip, ")")
print("Port:", port)
print("Menunggu koneksi")

data_payload = 2048


def send_message(client_address, message):
    sock.sendto(message.encode('utf-8'), client_address)


def receive_message():
    data, address = sock.recvfrom(data_payload)
    return data.decode(), address


while True:
    data, address = receive_message()
    print("Terhubung dengan client", address)

    while True:
        if data == "[e]":
            message = "Keluar Dari Chat Room!"
            send_message(address, message)
            print("\n")
            break
        print(f"Client {data}")
        message = input("Server: ")
        send_message(address, message)
        data, address = receive_message()

    print("Closing connection to the client")

sock.close()