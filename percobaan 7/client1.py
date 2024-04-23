import socket
import sys
import argparse
# host = input("Masukkan IP Server: ")
# port = int(input("Masukkan Port Server: "))
host = 'localhost'
port = 9900
def echo_client(port):
    """A simple echo client"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print(f"Connecting to {host} port {port}")
    sock.connect(server_address)
    while True:
        # Send data
        message = input("Client: ")
        print(f"Sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        data = sock.recv(9000).decode('utf-8')
        print(f"Received: {data}")
        if data == 'exit':
            print("Koneksi dari server terputus")
            sock.close()
            break
echo_client(port)
