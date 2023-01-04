# list makanan dengan 2 dimensi
list_makanan = [
    ['bakwan','tempe','tahu'],
    ['nasi uduk','nasi pecel','sate padang']
]

# bagaimana memprint nasi pecel?
print(list_makanan[1][1])

#cetak semua makanan
for i in list_makanan:
    for detail_makanan in i :
        print(detail_makanan)


