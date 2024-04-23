import socket
def get_remote_machine_info():
    remote_host = "www.python.org" 
    get_remote_machine_info()
    try:
        print ("IP address of %s: %s" % (remote_host,
        socket.gethostbyname (remote_host)))
    except socket.error as err_msg: print ("%s:%s" % (remote_host, err_msg))
if __name_== '_main_':
    get_remote_machine_info()
