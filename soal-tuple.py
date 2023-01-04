# membuat tuple menggunakan buka tutup kurung ("value",..)
gorengan = ('bakwan','combro','misro')              
sop = ('sop iga','sop buntut','sop kaki')
nasi = ('nasi uduk','nasi goreng','nasi rames')
# tuple di dlm tuple
makanan = (gorengan, sop, nasi)
#index          0      1    2

#cetak gorengan dari variabel makanan dikeluarkan dari buka tutup kurung
for i in makanan[0]:
    print(i)

# cetak sop buntut
print(sop[1])

#cetak nasi rames
print(nasi[2])

#cetak seluruh dan pastikan keluar
for i in makanan:
    for detail_makanan in i :
        print(detail_makanan)
