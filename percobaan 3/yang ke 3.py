def menu ():
    print ("Menu")
    print ("---------------------------------------")
    print ("1. LuasPersegi")
    print ("2. LuasPersegiPanjang")
    print ("3. LuasJajarGenjang")
    print ("4. LuasLingkaran")
    print ("5. LuasSegitiga")
    print ("6.Keluar")
    miliho= input("masukaan pilihan:")
    if(miliho=="1"):
        LuasPersegi()
    elif(miliho=="2"):
        LuasPersegiPanjang()
    elif(miliho=="3"):
        LuasJajarGenjang()
    elif(miliho=="4"):
        LuasLingkaran()
    elif(miliho=="5"):
        LuasSegitiga()
    elif(miliho=="6"):
        print ("terima kasih")

        exit()
    else:
        exit()
        
        

    
def LuasPersegi():
    print ("Program Mencari Luas Persegi")
    print ("------------------------------")
    x=float(input ("Panjang sisi: "))
    luas= x*x
    print (" ")
    print ("Luas Perseginya adalah :",luas, "cm2")
    print (" ")
    print ("Mau Coba Lagi[Y/N]")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()
def LuasPersegiPanjang():
    print ("Program Mencari Luas Persegi Panjang")
    print ("---------------------------------------")
    p= float(input ("Masukan Panjang: "))
    print (" ")
    l= float(input ("Masukan Lebar: "))
    print (" ")
    luas= p*l
    print (" ")
    print ("Luas PersegiPanjangnya adalah :",luas, "cm2")
    print (" ")
    print ("Mau Coba Lagi[Y/N]")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()
def LuasJajarGenjang():
    print ("Program Mencari Luas Jajar Genjang")
    print ("---------------------------------------")
    a= float(input ("Masukan Alas: "))
    print (" ")
    t= float(input ("Masukan Tinggi: "))
    print (" ")
    luas= a*t
    print (" ")
    print ("Luas Jajar Genjang adalah :",luas, "cm2")
    print (" ")
    print ("Mau Coba Lagi[Y/N]")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()
def LuasLingkaran():
    print ("Program Mencari Luas Lingkaran")
    print ("---------------------------------------")
    pi=3.14
    r= float(input ("Masukan Jari-jari: "))
    print (" ")
    luas= pi * (r ** 2)
    print (" ")
    print ("Luas Lingkaran adalah :",luas, "cm2")
    print (" ")
    print ("Mau Coba Lagi[Y/N]")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()
def LuasSegitiga():
    print ("Program Mencari Luas Segitiga")
    print ("---------------------------------------")
    od=0.5
    a= float(input ("Masukan Alas: "))
    print (" ")
    t= float(input ("Masukan Tinggi: "))
    print (" ")
    luas= 0.5 *(a * t)
    print (" ")
    print ("Luas Jajar Genjang adalah :",luas, "cm2")
    print (" ")
    print ("Mau Coba Lagi[Y/N]")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

menu()
        
    
