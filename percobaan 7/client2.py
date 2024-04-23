import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048


def echo_client(port):
    """A simple echo client"""
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    message = 'This is the message. It will be repeated.'

    try:
        # Send data
        message = "Test message. This will be echoed"
        print(f"Sending {message}")
        sent = sock.sendto(message.encode('utf-8'), server_address)

        # Receive response
        data, server = sock.recvfrom(data_payload)
        print(f"Received {data.decode()}")
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    echo_client(9900)
