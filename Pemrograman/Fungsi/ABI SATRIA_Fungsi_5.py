#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Contoh penggunaan
indeks_fibonacci = int(input("Masukkan indeks Fibonacci: "))
hasil_fibonacci = fibonacci(indeks_fibonacci)
print(f"Bilangan Fibonacci ke-{indeks_fibonacci} adalah {hasil_fibonacci}.")
