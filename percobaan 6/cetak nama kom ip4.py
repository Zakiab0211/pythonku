import socket
def print_machine_info():
    host_name=socket.gethostname ()
    ip_address=socket.gethostbyname (host_name)
    print("host name", host_name)
    print("ip", ip_address)
print_machine_info()
