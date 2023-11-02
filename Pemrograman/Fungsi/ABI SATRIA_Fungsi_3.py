#nama : ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 11
#Soal: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def pangkat(bilangan, eksponen):
    hasil = bilangan ** eksponen
    return hasil

# Contoh penggunaan
bilangan_user = int(input("Masukkan bilangan: "))
eksponen_user = int(input("Masukkan eksponen: "))
hasil_pangkat = pangkat(bilangan_user, eksponen_user)
print(f"{bilangan_user} pangkat {eksponen_user} adalah {hasil_pangkat}.")
