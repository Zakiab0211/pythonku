# Deklarasi fungsi
def pembelian( var_jumlah, var_harga):
    var_jumlah = int(var_jumlah)
    var_harga = int(var_harga ) 
    return var_jumlah * var_harga

def fungsi_perulangan():
    # sourcery skip: for-index-underscore, remove-unit-step-from-range
    n = int(input("\nMasukan Jumlah Barang: "))
    var_hasil_perulangan = 0
    for x in range(n):
        var_nama = input("Nama Barang: ")
        var_jumlah = input("jumlah: ")
        var_harga = input("Harga: ")
        var_hasil_perulangan += int(pembelian( var_jumlah, var_harga))
        print("total harga barang :", int(pembelian( var_jumlah, var_harga)))
            
    return var_hasil_perulangan 

var_total_harga = fungsi_perulangan()

print("------------Total----------")
print("Total Harga:", var_total_harga)
