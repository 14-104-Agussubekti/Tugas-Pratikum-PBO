import csv

# Inisialisasi dictionary untuk menyimpan data mahasiswa
mahasiswa = {}  # Membuat dictionary kosong untuk menyimpan data mahasiswa dengan NIM sebagai key

# Fungsi untuk menambah data mahasiswa
def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:  # Mengecek apakah NIM sudah ada
        print("NIM sudah terdaftar.")
        return # Keluar dari fungsi jika sudah ada Nim yang di input
    nama = input("Masukkan Nama: ")
    nilai = input("Masukkan Nilai: ")
    try:
        nilai = float(nilai)  # Casting
    except ValueError:
        print("Nilai harus berupa angka.")
        return
    mahasiswa[nim] = {"nama": nama, "nilai": nilai}  # Menambahkan data mahasiswa ke dictionary
    print("Mahasiswa berhasil ditambahkan!")

# Fungsi untuk menampilkan semua data mahasiswa
def tampilkan_semua_mahasiswa():
    if not mahasiswa:  # Memeriksa apakah dictionary mahasiswa kosong
        print("Belum ada data mahasiswa.")
        return  # Keluar dari fungsi jika kamus kosong
    print("==== DATA MAHASISWA ====")
    print("NIM      | Nama  | Nilai")
    print("-------------------------")
    for nim, data in mahasiswa.items(): # Perulangan untuk setiap data yang ada
        print(f"{nim}  | {data['nama']} | {data['nilai']}")  # Menampilkan data mahasiswa dalam format tabel

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa():
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in mahasiswa:  # Memeriksa apakah NIM ada di kamus
        data = mahasiswa[nim]  # Mengambil data mahasiswa berdasarkan NIM
        print("Data Mahasiswa:")
        print(f"NIM: {nim}")
        print(f"Nama: {data['nama']}")
        print(f"Nilai: {data['nilai']}")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk mengedit data mahasiswa
def edit_mahasiswa():
    nim = input("Masukkan NIM yang ingin diedit: ")
    if nim in mahasiswa:
        nama_baru = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
        nilai_baru = input("Nilai baru (kosongkan jika tidak ingin mengubah): ")
        if nama_baru:  # Jika nama baru diisi
            mahasiswa[nim]['nama'] = nama_baru  # Mengupdate nama di Dictionary
        if nilai_baru:  # Jika nilai baru diisi
            try:
                mahasiswa[nim]['nilai'] = float(nilai_baru)  # Mengupdate nilai di kamus
            except ValueError:
                print("Nilai harus berupa angka.")
                return
        print("Data berhasil diperbarui!")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk menghapus data mahasiswa
def hapus_mahasiswa():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in mahasiswa:  # Memeriksa apakah NIM ada di kamus
        del mahasiswa[nim]  # Menghapus entri mahasiswa dari kamus
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan.")

# Fungsi untuk menyimpan data ke file
def simpan_ke_file():
    with open('mahasiswa.csv', 'w', newline='') as file:  # Membuka file CSV untuk ditulis
        writer = csv.writer(file)  # Membuat objek writer untuk menulis ke file CSV
        writer.writerow(["NIM", "Nama", "Nilai"])  # Menulis header kolom ke file
        for nim, data in mahasiswa.items():  # Melakukan iterasi pada kamus mahasiswa
            writer.writerow([nim, data['nama'], data['nilai']])  # Menulis data mahasiswa ke file
    print("Data mahasiswa telah disimpan dalam file 'mahasiswa.csv'")

# Fungsi untuk memuat data dari file
def muat_dari_file():
    try:
        with open('mahasiswa.csv', 'r') as file:  # Membuka file CSV untuk dibaca
            reader = csv.DictReader(file)  # Membuat objek reader untuk membaca file CSV sebagai kamus
            for row in reader:  # Melakukan iterasi pada setiap baris di file
                nim = row['NIM']  # Mengambil NIM dari baris
                nama = row['Nama']  # Mengambil nama dari baris
                nilai = float(row['Nilai'])  # Mengambil nilai dan mengkonversinya ke float
                mahasiswa[nim] = {"nama": nama, "nilai": nilai}  # Menambahkan data ke kamus
        print("Data mahasiswa telah dimuat dari file 'mahasiswa.csv'")  # Menampilkan pesan sukses
    except FileNotFoundError:  # Menangkap kesalahan jika file tidak ditemukan
        print("File 'mahasiswa.csv' tidak ditemukan. Memulai dengan data kosong.")  # Menampilkan pesan

# Fungsi utama untuk menampilkan menu dan mengelola pilihan pengguna
def main():
    muat_dari_file()  # Memuat data dari file saat program dimulai
    while True:
        print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa Berdasarkan NIM")
        print("4. Edit Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Simpan ke File")
        print("7. Keluar")
        pilihan = input("Pilihan: ")

        if pilihan == '1':
            tambah_mahasiswa()
        elif pilihan == '2':
            tampilkan_semua_mahasiswa()
        elif pilihan == '3':
            cari_mahasiswa()
        elif pilihan == '4':
            edit_mahasiswa()
        elif pilihan == '5':
            hapus_mahasiswa()
        elif pilihan == '6':
            simpan_ke_file()
        elif pilihan == '7':
            simpan_ke_file()
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":  # Memeriksa apakah file dijalankan langsung (bukan diimpor)
    main()  # Memanggil fungsi utama untuk memulai program