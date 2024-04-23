import socket
from binascii import hexlify

def find_service_name():
    protocolname = 'tcp'
    website_ip = input("Masukkan alamat IP: ")
    website_port = int(input("Masukkan port protokol: "))
    try:
        service_name = socket.getservbyport(website_port, protocolname)
        print("Port: %s => Service name: %s" % (website_port, service_name))
    except OSError:
        print("Port: %s => Unknown service" % website_port)

def get_remote_machine_info():
    remote_host = input("Masukkan alamat website: ")
    try:
        print("Anda mengakses :%s " % (remote_host))
        print("Dengan alamat IP :%s " % (socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print("%s:%s" % (remote_host, err_msg))
def print_machine_info():
    host_name=socket.gethostname ()
    ip_address=socket.gethostbyname (host_name)
    print("Dari Komputer:", host_name)
    print("Alamat IP:", ip_address)
    
def convert_ip4_address():
    ip_addr = input("Masukkan alamat IP: ")
    packed_ip_addr = socket.inet_aton(ip_addr)
    hex_ip_addr = hexlify(packed_ip_addr).decode()
    binary_ip_addr = '.'.join(format(int(x), '08b') for x in packed_ip_addr)
    print("IP Address: %s => Packed: %s, Hex: %s, Binary: %s" % (ip_addr, hex_ip_addr, hex_ip_addr, binary_ip_addr))

if __name__ == '__main__':
    dt = "y"
    while dt == "y":
        print("MENU PILIHAN")
        print("1. Mengetahui service dan protokol")
        print("2. Mengetahui alamat IP")
        print("3. Mengubah alamat IP")
        menu = int(input("Masukkan pilihan: "))
    
        if menu == 1:
            find_service_name()
        elif menu == 2:
            get_remote_machine_info()
            print_machine_info()
        elif menu == 3:
            convert_ip4_address()
        else:
            print("Pilihan tidak valid.")
        
        pil = input("Anda ingin mengulang (Y/T)? ")
        if pil.lower() == "y":
            dt = "y" 
        else:
            break
