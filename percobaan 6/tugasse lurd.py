dt = "y"
while dt == "y":
        print ("MENU PILIHAN")
        print("1. Mengetahui service dan protokol")
        print ("2. Mengetahui alamat IP")
        menu = int(input("Masukkan pilihan:"))
    
        if menu == 1:
                find_service_name()
        elif menu == 2:
                get_remote_machine_info()
        pil = input ("Anda ingin mengulang (Y/T)")
        if pil == "y":
                dt == "y" 
        else:
                break
