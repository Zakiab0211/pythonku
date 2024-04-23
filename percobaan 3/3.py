#Deklarasi Fungsi Perulangan
def fungsi_perulangan():
    var_hasil_perulangan = 0
    for i in range(1,3):
        print("--------Nilai ke ",i,"--------")
        var_harian = input("Nilai Harian:")
        var_uts = input("Nilai UTS:")
        var_uas = input("Nilai UAS:")

        #Pemanggilan fungsi Penjumlahan
        var_hasil_perulangan += (int(fungsi_total_nilai(var_harian,var_uts,var_uas)))
        return var_hasil_perulangan /i

#Pemanggilan fungsi perulangan
var_total = fungsi_perulangan()

print("--------Total Nilai--------")
print("total nilai yang didapat : ",var_total)

#Pemanggilan Fungsi Percabangan
print("Total Nilai Dalam Huruf :",fungsi_percabangan(var_total))

