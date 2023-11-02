#nama : ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

# Contoh penggunaan
bilangan_user = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
hasil_faktorial = faktorial(bilangan_user)
print(f"Faktorial dari {bilangan_user} adalah {hasil_faktorial}.")
