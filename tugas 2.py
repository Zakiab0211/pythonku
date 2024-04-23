# Nama Toko
print("DQ Mart")
#kode untuk menjalankan program
namaitem = str(input("Masukkan nama item: "))
hargaitem = int(input("Masukkan harga item : "))
jumlah = int(input("Masukkan jumlah item yang dibeli : "))
bayar = int(input("Masukkan jumlah uang yang dibayar : "))
Total= (hargaitem*jumlah-bayar)
print("Total kembalian: ","Rp.", Total)
