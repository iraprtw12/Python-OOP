# membuat class dengan kata kunci "class"

class Mahasiswa:
    #atribut
    # konstruktor
    def __init__(self, nim, nama, rombel) :
        # variabel objek
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    #method
    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")

     # class mahasiswa memiliki 3 atribut dan 1 fungsi

    def cetak(self):
        print("nama :", self.nama)
        print("nim :", self.nim)
        print("rombel :", self.rombel)
        
# membuat objek
mahasiswa1 = Mahasiswa("0110222162", "ira", "ti05")
# mencetak atribut
mahasiswa1.cetak()
mahasiswa1.lulus(95)

# objek ke 2
mahasiswa2 = Mahasiswa("08989796", "fatyah", "ti02")
# mencetak atribut
mahasiswa2.cetak()
mahasiswa2.lulus(85)

#print(help(mahasiswa1))




