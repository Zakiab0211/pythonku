print("Selamat datang di Program Biodata")
print("================================")

nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

teks = f"\nNama: {nama}\nUmur: {umur}\nAlamat: {alamat}\n---"

file_bio = open("biodata.txt", "a")
file_bio.write(teks)
file_bio.close()

print("Biodata telah berhasil ditambahkan ke dalam file biodata.txt")