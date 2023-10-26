#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

def tentukan_hasil_nilai(tugas, ujian):
    if tugas > 70 and ujian > 60:
        hasil = "Lulus"
    else:
        hasil = "Gagal"
    return hasil

def main():
    nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
    nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))

    hasil_nilai = tentukan_hasil_nilai(nilai_tugas, nilai_ujian)

    print(f"Nilai Tugas: {nilai_tugas}")
    print(f"Nilai Ujian: {nilai_ujian}")
    print(f"Hasil Nilai: {hasil_nilai}")

if __name__ == "__main__":
    main()