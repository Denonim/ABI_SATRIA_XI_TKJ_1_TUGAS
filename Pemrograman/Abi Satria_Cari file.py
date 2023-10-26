#nama: ABI SATRIA
#Kelas: XI TKJ 1
#Absen: 1
#Soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

import os

def cek_keberadaan_file(nama_file, daftar_file_di_server):
    if nama_file in daftar_file_di_server:
        print("File sudah ada.")
    else:
        print("File belum ada.")

nama_file = "data.txt"

daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

cek_keberadaan_file(nama_file, daftar_file_di_server)