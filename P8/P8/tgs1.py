print("Selamat datang di Program Biodata")
print("================================")

nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

teks = f"Nama: {nama}\nUmur: {umur}\nAlamat: {alamat}"

file_bio = open("biodata.txt", "w")
file_bio.write(teks)
file_bio.close()

print("Biodata telah berhasil disimpan ke dalam file biodata.txt")kadad