#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebagai seorang pengembang perangkat lunak, Anda perlu membuat program sederhana yang menghitung bonus tahunan karyawan berdasarkan performa mereka.

def hitung_bonus(performa, gaji_tahunan):
    bonus = (
        0.20 * gaji_tahunan if performa == 5 else
        0.10 * gaji_tahunan if performa == 4 else
        0.05 * gaji_tahunan if performa == 3 else
        0.02 * gaji_tahunan if performa == 2 else
        0  )
    return bonus

def main():
    performa = int(input("Masukkan nilai performa karyawan (1-5): "))

    gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

    bonus = hitung_bonus(performa, gaji_tahunan)

    print(f"Performa karyawan: {performa}")
    print(f"Gaji tahunan karyawan: {gaji_tahunan}")
    print(f"Bonus tahunan: {bonus}")

if __name__ == "__main__":
    main()