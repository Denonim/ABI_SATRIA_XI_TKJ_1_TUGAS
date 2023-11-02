#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal:  Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def total_deret_ganjil(batas):
    total = sum(range(1, 2 * batas, 2))
    return total

# Contoh penggunaan
batas_user = int(input("Masukkan batas deret ganjil: "))
hasil_total = total_deret_ganjil(batas_user)
print(f"Total deret bilangan ganjil hingga batas {batas_user} adalah {hasil_total}.")
