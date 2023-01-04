# buat fungsi menampilkan siswa yang lulus nilai > 65
hasil_akhir = [
    {'nama':'reza', 'nilai':70},
    {'nama':'cut', 'nilai':63},
    {'nama':'dian', 'nilai':80},
    {'nama':'badu', 'nilai':40}
]
def lulus_saja(data):
    for hasil in data:
        if hasil['nilai'] > 65:
            print(hasil['nama'])
lulus_saja(hasil_akhir)