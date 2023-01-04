# membuat list ditandai dengan [ ]
buah = ["mangga","melon","jeruk","apel"]

# untuk mengaksesnya menggunakan index
# dan index dimulai dari 0

# cetak mangga
#print(buah[0])

# menambah list menggunakan append ("value")
buah.append("pisang")
#print(buah)

# mengubah list
# variabel[index ke berapa] = nilai baru
buah[0] = "jambu"
#print(buah)

# menghapus list
# del buah[index yg mau diapus]
#del buah[1]
#print(buah)

# mengambil data akhir menggunakan pop
#print(buah.pop())

# mengambil jumlah data dari list
# menggunakan len()
#print(len(buah))

# menyisipkan data sesuai index yg di ingin
buah.insert(1,"duku")
#print(buah)

# menagmbil seluruh data di list menggunakan perulangan for
for i in buah:
    print(i)