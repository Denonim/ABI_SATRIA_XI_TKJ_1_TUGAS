# Input total belanjaan pelanggan
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi diskon
diskon = 0

# Hitung diskon berdasarkan aturan
if total_belanjaan > 500000:
    diskon = 0.1  # 10% diskon
elif total_belanjaan >= 300000:
    diskon = 0.05  # 5% diskon

# Hitung total pembayaran setelah diskon
total_pembayaran = total_belanjaan - (total_belanjaan * diskon)

# Tampilkan total pembayaran
print(f"Total belanjaan: Rp {total_belanjaan:,.2f}")
print(f"Diskon: {diskon * 100}%")
print(f"Total pembayaran setelah diskon: Rp {total_pembayaran:,.2f}")
