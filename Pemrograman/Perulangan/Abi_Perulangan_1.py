#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

ayam = 100
bulan = 0

while ayam <= 200:
    bulan += 1
    pertambahan_ayam = 0.05 * ayam
    ayam += pertambahan_ayam

print("Jumlah ayam melebihi 200 ekor pada bulan ke-", bulan)
