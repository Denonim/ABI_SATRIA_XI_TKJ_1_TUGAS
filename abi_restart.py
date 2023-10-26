#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

def cek_perlu_restart(pembaruan_perangkat_lunak):
    if pembaruan_perangkat_lunak.lower() == "ya":
        print("Sistem perlu di-restart.")
    else:
        print("Sistem tidak perlu di-restart.")

def main():
    pembaruan_perangkat_lunak = input("Apakah ada pembaruan perangkat lunak? (ya/tidak): ")

    cek_perlu_restart(pembaruan_perangkat_lunak)

if __name__ == "__main__":
    main()