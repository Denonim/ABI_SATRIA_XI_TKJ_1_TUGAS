#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarak = 5  # Jarak awal dalam kilometer
minggu = 0

while jarak <= 10:
    minggu += 1
    pertambahan_jarak = 0.10 * jarak
    jarak += pertambahan_jarak

print("Pelari berlari lebih dari 10 kilometer setelah", minggu, "minggu.")
