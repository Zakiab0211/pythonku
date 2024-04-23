# fungsi untuk menghitung volume balok
def volume_balok(p, l, t):
    return p * l * t

# fungsi untuk menghitung volume kubus
def volume_kubus(s):
    return s ** 3

# fungsi untuk menghitung volume kerucut
def volume_kerucut(r, t):
    return 1/3 * 3.14 * r**2 * t

# fungsi untuk menghitung volume tabung
def volume_tabung(r, t):
    return 3.14 * r**2 * t

# fungsi untuk menghitung volume bola
def volume_bola(r):
    return 4/3 * 3.14 * r**3

# tampilkan menu pilihan
print("Program Volume Bangun Ruang")
print("1. Balok")
print("2. Kubus")
print("3. Kerucut")
print("4. Tabung")
print("5. Bola")

# minta pengguna memilih bangun ruang
pilihan = int(input("Pilih jenis bangun ruang (1-5): "))

# evaluasi pilihan pengguna dan minta pengguna memasukkan dimensi yang diperlukan
if pilihan == 1:
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume = volume_balok(panjang, lebar, tinggi)
    print("Volume Balok = ", volume)
elif pilihan == 2:
    sisi = float(input("Masukkan sisi kubus: "))
    volume = volume_kubus(sisi)
    print("Volume Kubus = ", volume)
elif pilihan == 3:
    jari_jari = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    volume = volume_kerucut(jari_jari, tinggi)
    print("Volume Kerucut = ", volume)
elif pilihan == 4:
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    volume = volume_tabung(jari_jari, tinggi)
    print("Volume Tabung = ", volume)
elif pilihan == 5:
    jari_jari = float(input("Masukkan jari-jari bola: "))
    volume = volume_bola(jari_jari)
    print("Volume Bola = ", volume)
else:
    print("Pilihan tidak valid")
