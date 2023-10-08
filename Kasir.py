# Fungsi untuk daftar menu makanan
def makanan():
      global total_makan, jumlah_porsi, nama_makanan
      
# Fungsi untuk daftar menu minuman
def minuman():
      global total_minum, jumlah_gelas, nama_minuman
      
print("|===============================|")
print("| Program Mesin Kasir Sederhana |")
print("|===============================|")
print("|    :  Pilih Menu Makanan   :  |")
print("|===============================|")
print("| 1. Nasi Lemak        Rp.10000 |")
print("| 2. Ayam Kecap        Rp.10000 |")
print("| 3. Mie Goreng        Rp.5000  |")
print("| 4. Sayur Lobak       Rp.7000  |")
print("| 5. Ikan Goreng       Rp.15000 |")
print("|===============================|")
menu_makanan = int(input(" Pilih Menu (!/2/3/4/5) : "))
jumlah_porsi = int(input(" Berapa Porsi : "))

if menu_makanan == 1:
      total_makan = jumlah_porsi * 10000
      print(" Nasi Lemak", jumlah_porsi, "Porsi : Rp.", total_makan)
      nama_makanan = ("Nasi Lemak")
elif menu_makanan == 2:
      total_makan = jumlah_porsi * 10000
      print(" Ayam Kecap", jumlah_porsi, "Porsi : Rp.", total_makan)
      nama_makanan = ("Ayam Kecap")
elif menu_makanan == 3:
      total_makan = jumlah_porsi * 5000
      print(" Mie Goreng", jumlah_porsi, "Porsi : Rp.", total_makan)
      nama_makanan = ("Mie Goreng")
elif menu_makanan == 4:
      total_makan = jumlah_porsi * 7000
      print(" Sayur Lobak", jumlah_porsi, "Porsi : Rp.", total_makan)
      nama_makanan = ("Sayur Lobak")
elif menu_makanan == 5:
      total_makan = jumlah_porsi * 15000
      print(" Ikan Goreng", jumlah_porsi, "Porsi : Rp.", total_makan)
      nama_makanan = ("Ikan Gorng")
else:
      print(" Pilihan Tidak Tersedia")
      
print()
print("|===============================|")
print("|   :  Pilih Menu Minuman  :    |")
print("|===============================|")
print("| 1. Es Timun          Rp.4000  |")
print("| 2. Es Coklat         Rp.4000  |")
print("| 3. Nutrisari         Rp.5000  |")
print("| 4. Kopi Susu         Rp.5000  |")
print("|===============================|")
menu_minuman = int(input(" Pilih Menu (1/2/3/4) : "))
jumlah_gelas = int(input(" Berapa Gelas : "))

if menu_minuman == 1:
      total_minum = jumlah_gelas * 4000
      print(" Es Timun", jumlah_gelas, " Gelas : Rp.", total_minum)
      nama_minuman = (" Es Teh")
elif menu_minuman ==2:
      total_minum = jumlah_gelas * 4000
      print(" Es Coklat", jumlah_gelas, " Gelas : Rp.", total_minum)
      nama_minuman = (" Es Coklat")
elif menu_minuman ==3:
      total_minum = jumlah_gelas * 5000
      print(" Nutrisari", jumlah_gelas, " Gelas : Rp.", total_minum)
      nama_minuman = (" Nutrisari")
elif menu_minuman ==4:
      total_minum = jumlah_gelas * 5000
      print(" Kopi Susu", jumlah_gelas, " Gelas : Rp.", total_minum)
      nama_minuman = (" Kopi Susu")
else:
      print(" Pilihan Tidak Tersedia")
      
# Proses menghitung semua harga yang harus dibayar
makanan()
minuman()
jumlah_semuanya = total_makan + total_minum

# Daftar pembelian
print()
print("|===============================|")
print("|       Daftar Pembelian        |")
print("|===============================|")
print("| Makanan  :", nama_makanan,"\t|")
print("| Porsi    :", jumlah_porsi,"\t                |")
print("| Minuman  :", nama_minuman,"\t|")
print("| Gelas    :", jumlah_gelas,"\t                |")
print("|===============================|")
print("|   Jadi yang Harus Di Bayar    |")
print("|===============================|")
print("|  Total   :", jumlah_semuanya,"             |")
print("|===============================|")
print()

