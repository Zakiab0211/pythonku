import socket
import sys
import argparse
host = 'localhost'
data_payload = 2048
backlog = 1
port = 9900


def echo_server(port):
    """A simple echo server"""

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print(f"Starting up echo server on port {server_address}")
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    print("Menunggu pesan dari client")
    client, address = sock.accept()
    while True:
        data = client.recv(9000).decode('utf-8')
        print(f"Pesan dari client: {data}")
        message = input("Server: ")
        client.sendall(message.encode('utf-8'))
        # End connection
        if data == 'exit':
            print("Memutuskan koneksi ke client")
            client.close()
            break
echo_server(port)
