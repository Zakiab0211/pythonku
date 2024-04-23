def hitung_nilai():
    print ("PROGRAM PYTHON MENGHITUNG NILAI TERKECIL DAN TERBESAR SERTA NILAI RATA-RATA")
    n = int(input("\nMasukkan Jumlah Bilangan ="))
    bil =[]
    tot = 0
    for x in range(n):
        m = x+1
        a = int(input("Bilangan ke %d = "%m))
        bil.append(a)
        tot += bil[x]
        rata2 = tot / n

    print("\nBilangan Terkecil : %d" %min(bil))
    print("\nBilangan Terbesar : %d" %max(bil))
    print("Nilai Rata-rata : %0.2f" %rata2)

hitung_nilai()
