import socket
import sys

host = 'localhost'


def echo_client(port):
    """A simple echo client"""
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    # send data
    try:
        _extracted_from_echo_client_13(sock)
    except socket.error as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"Other exception: {str(e)}")
    finally:
        print("Closing connection to the server")
        sock.close()


# TODO Rename this here and in `echo_client`
def _extracted_from_echo_client_13(sock):
    # send data
    message = "Test message. This will be echoed"
    print(f"Sending {message}")
    sock.sendall(message.encode('utf-8'))
    # look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"Received: {data}")


if __name__ == '__main__':
    # parser=argparse.ArgumentParser(description='Socket Server Example')
    # parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    # given_args=parser.parse_args()
    # port=given_args.port
    echo_client(9900)
