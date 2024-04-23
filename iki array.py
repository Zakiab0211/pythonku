import threading

array1 = [6, 9, 1, 2, 3]
array2 = [7, 11, 6, 4, 3]
array3 = [5, 4, 3, 2, 1]

result = [0] * len(array1)  # array kosong untuk menampung hasil penjumlahan

# fungsi yang akan dieksekusi oleh setiap thread
def add_arrays(start_index, end_index):
    for i in range(start_index, end_index):
        result[i] = array1[i] + array2[i] + array3[i]

# membuat 5 thread dengan tugas yang berbeda-beda
threads = []
for i in range(5):
    start_index = i * (len(array1) // 5)
    end_index = start_index + (len(array1) // 5)
    if i == 4:  # menangani kasus terakhir, agar indeks terakhir dihitung semua
        end_index = len(array1)
    t = threading.Thread(target=add_arrays, args=(start_index, end_index))
    threads.append(t)

# menjalankan thread-thread yang sudah dibuat
for t in threads:
    t.start()

# menunggu thread-thread selesai bekerja
for t in threads:
    t.join()

# mencetak hasil penjumlahan
print("Hasil = ", end="")
for i in range(len(result)):
    print(result[i], end=" ")
print()

# mencetak total
print("Total: ", sum(result))
