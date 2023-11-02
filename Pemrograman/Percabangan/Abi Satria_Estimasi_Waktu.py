#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

from datetime import datetime

def cek_waktu_selesai(estimasi_selesai, target_selesai):
    estimasi_selesai = datetime.strptime(estimasi_selesai, "%d-%m-%Y")
    target_selesai = datetime.strptime(target_selesai, "%d-%m-%Y")

    if target_selesai <= estimasi_selesai:
        print("Tepat waktu")
    else:
        print("Terlambat")

estimasi_waktu = input("Masukkan estimasi waktu selesai (format: DD-MM-YYYY): ")
tanggal_target = input("Masukkan tanggal target selesai (format: DD-MM-YYYY): ")

cek_waktu_selesai(estimasi_waktu, tanggal_target)