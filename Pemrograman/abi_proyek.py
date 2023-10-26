#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal:Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.

def tentukan_status_proyek(status_persiapan):
    if status_persiapan.lower() == "siap":
        print("Proyek diluncurkan.")
    elif status_persiapan.lower() == "tunda":
        print("Proyek ditunda.")
    else:
        print("Status persiapan tidak valid.")

def main():
    status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

    tentukan_status_proyek(status_persiapan)

if __name__ == "__main__":
    main()