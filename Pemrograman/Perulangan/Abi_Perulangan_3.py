#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

investasi = 10000
tahun = 0

while investasi <= 20000:
    tahun += 1
    pertumbuhan_investasi = 0.06 * investasi
    investasi += pertumbuhan_investasi

print("Dibutuhkan", tahun, "tahun agar nilai investasi melebihi 20,000 dollar.")
