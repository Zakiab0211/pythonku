print ("Selamat datang di Program Biodata")
print ("=================================")

nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

teks = "Nama: {}\nUmur: {}\nAlamat: {}\n---".format(nama, umur, alamat)

file_bio = open("biodata.txt", "a")

file_bio.write(teks)

file_bio.close()