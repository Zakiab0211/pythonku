import socket
from binascii import hexlify

port = int(input("Masukkan port protokol: ")) 
protocolname = 'tcp'
print ("Port: %s => service name: %s" % (port, socket.getservbyport
                                         (port, protocolname)))
