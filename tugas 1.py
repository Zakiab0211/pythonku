nama  = input("Masukkan Nama:")
nrp   = int(input("Masukkan NRP: "))
nilai = int(input("Masukkan Nilai : "))

if nilai >= 81 and nilai <= 100:
    nilai_huruf = "A"
    bobot = 4
    kategori = "Istimewa"
elif nilai >= 71 and nilai <= 80:
    nilai_huruf = "AB"
    bobot = 3.5
    kategori = "Sangat baik"
elif nilai >= 66 and nilai <= 70:
    nilai_huruf = "B"
    bobot = 3
    kategori = "Baik"
elif nilai >= 61 and nilai <= 65:
    nilai_huruf = "BC"
    bobot = 2.5
    kategori = "Cukup baik"
elif nilai >= 56 and nilai <= 60:
    nilai_huruf = "C"
    bobot = 2
    kategori = "Cukup"
elif nilai >= 41 and nilai <= 55:
    nilai_huruf = "D"
    bobot = 1
    kategori = "Kurang"
else:
    nilai_huruf = "E"
    bobot = 0
    kategori = "Sangat kurang"
print("Nama Mahasiswa:", nama)
print("NRP:",nrp)
print("Nilai Anda:", nilai)
print("Nilai huruf :", nilai_huruf)
print("Bobot :", bobot)
print("Kategori :", kategori)
