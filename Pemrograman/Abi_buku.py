#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman.

def tentukan_jenis_pinjaman(durasi_peminjaman):
    if durasi_peminjaman <= 7:
        jenis_pinjaman = "Peminjaman Pendek"
    elif 7 < durasi_peminjaman <= 30:
        jenis_pinjaman = "Peminjaman Menengah"
    else:
        jenis_pinjaman = "Peminjaman Panjang"
    return jenis_pinjaman

def main():
    durasi_peminjaman = int(input("Masukkan durasi peminjaman buku dalam hari: "))

    jenis_pinjaman = tentukan_jenis_pinjaman(durasi_peminjaman)

    print(f"Durasi Peminjaman: {durasi_peminjaman} hari")
    print(f"Jenis Pinjaman: {jenis_pinjaman}")

if __name__ == "__main__":
    main()