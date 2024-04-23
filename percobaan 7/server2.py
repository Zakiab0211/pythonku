import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048


def echo_server(port):
    """A simple echo server"""

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = (host, port)
    print(f"Starting up echo server on port {server_address}")
    sock.bind(server_address)

    while True:
        print("Waiting to receive message from client")
        data, address = sock.recvfrom(data_payload)
        print(f"received {len(data)} bytes from {address}")
        print(f"Data: {data.decode()}")

        # if data:
        data_input = input("Masukkan pesan: ")
        sent = sock.sendto(data_input.encode(), address)
        print(f"sent {sent} bytes back to {address}")


echo_server(9900)
