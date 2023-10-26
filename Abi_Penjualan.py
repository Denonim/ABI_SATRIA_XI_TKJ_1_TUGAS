#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal:Sebagai seorang analis data, Anda harus mengkategorikan produk berdasarkan penjualan bulanan.

def tentukan_kategori_produk(penjualan):
    if penjualan > 1000:
        kategori = "Produk Terlaris"
    elif 500 <= penjualan <= 1000:
        kategori = "Produk Populer"
    else:
        kategori = "Produk Biasa"
    return kategori

def main():
    penjualan = int(input("Masukkan jumlah penjualan bulanan: "))

    kategori_produk = tentukan_kategori_produk(penjualan)

    print(f"Penjualan Bulanan: {penjualan} unit")
    print(f"Kategori Produk: {kategori_produk}")

if __name__ == "__main__":
    main()