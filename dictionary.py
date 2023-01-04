# membuat dictionary
# { key : value}

data ={"nama":"ira pratiwi"}
#       key     value
print(data["nama"])

# mengakses value dengan funcion values()
nilai = {'firda':89,'inaya':80,'fawaz':95,'rahmah':100}
for skor in nilai.values():
    print(skor)
for nama in nilai.keys():
    print(nama)
for nama,nilai in nilai.items():
    print(nama,":", nilai)