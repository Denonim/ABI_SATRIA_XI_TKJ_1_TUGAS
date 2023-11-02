#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def jumlah_digit(bilangan):
    return sum(map(int, str(abs(bilangan))))

# Contoh penggunaan
bilangan_user = int(input("Masukkan bilangan: "))
hasil_jumlah_digit = jumlah_digit(bilangan_user)
print(f"Jumlah digit dari {bilangan_user} adalah {hasil_jumlah_digit}.")
