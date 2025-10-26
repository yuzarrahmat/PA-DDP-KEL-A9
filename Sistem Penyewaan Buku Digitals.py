import json
from prettytable import PrettyTable
import os
import pwinput
import time

logged_in_user = None

def BacaDataBuku():
    try:
        if not os.path.exists('PA DDP KEL A9/Buku.json'):
            with open('PA DDP KEL A9/Buku.json', 'w') as file:
                json.dump([], file)
            return []
        
        with open('PA DDP KEL A9/Buku.json', 'r') as file:
            data_buku = json.load(file)
        return data_buku
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def SimpanDataBuku(data):
    try:
        os.makedirs('PA DDP KEL A9', exist_ok=True)
        with open('PA DDP KEL A9/Buku.json', 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error menyimpan data buku: {e}")
        return False

def BacaDataAkun():
    try:
        if not os.path.exists('PA DDP KEL A9/Akun.json'):
            with open('PA DDP KEL A9/Akun.json', 'w') as file:
                json.dump([], file)
            return []
        
        with open('PA DDP KEL A9/Akun.json', 'r') as file:
            data_akun = json.load(file)
        return data_akun
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def SimpanDataAkun(data):
    try:
        os.makedirs('PA DDP KEL A9', exist_ok=True)
        with open('PA DDP KEL A9/Akun.json', 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error menyimpan data akun: {e}")
        return False

def menu_utama():
    while True:
        print("============================")
        print("======== MENU UTAMA ========")
        print("============================")
        print("1. Login User")
        print("2. Register User")
        print("3. Login Admin")
        print("4. Keluar")
        print("============================")
        pilihan = input("Pilih menu [1-4]: ")
        
        if pilihan == "1":
            login_user()
        elif pilihan == "2":
            register_user()
        elif pilihan == "3":
            login_admin()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

def register_user():
    data_akun = BacaDataAkun()
    
    e_mail = input("Masukkan email baru: ")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    
    try:
        saldo = int(input("Masukkan saldo awal: "))
    except ValueError:
        print("Saldo harus berupa angka!")
        return

    for akun in data_akun:
        if akun["username"] == username:
            print("Username sudah terdaftar!")
            return
    
    data_akun.append({
        "e_mail": e_mail,
        "username": username, 
        "password": password,
        "saldo": saldo
    })
    
    if SimpanDataAkun(data_akun):
        print("Registrasi user berhasil!")
    else:
        print("Gagal menyimpan data registrasi!")

def login_user():
    global logged_in_user
    data_akun = BacaDataAkun()
    
    e_mail = input("Masukkan email: ")
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")
    
    for akun in data_akun:
        if (akun["e_mail"] == e_mail and 
            akun["username"] == username and 
            akun["password"] == password):
            print("Login user berhasil!")
            logged_in_user = username
            menu_user()
            return True
    
    print("Login user gagal! Periksa kembali email, username, dan password Anda.")
    return False

def login_admin():
    admin_username = "admin"
    admin_password = "admin123"
    
    username = input("Masukkan username admin: ")
    password = pwinput.pwinput("Masukkan password admin: ")
    
    if username == admin_username and password == admin_password:
        print("Login admin berhasil!")
        menu_admin()
        return True
    else:
        print("Login admin gagal! Periksa kembali username dan password Anda.")
        return False

def menu_admin():
    while True:
        print("======== MENU ADMIN ========")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Ubah Buku")
        print("4. Hapus Buku")
        print("5. Logout")
        print("===========================")
        pilihan = input("Pilih menu [1-5]: ")
        
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_buku_admin()
        elif pilihan == "3":
            ubah_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            print("Logout admin berhasil.")
            break
        else:
            print("Pilihan tidak valid!")

def tambah_buku():
    buku = BacaDataBuku()
    
    ID_buku = input("Masukkan ID Buku: ")
    Judul_buku = input("Masukkan Judul Buku: ")
    Pengarang = input("Masukkan Pengarang: ")
    
    try:
        Biaya_sewa = int(input("Masukkan Biaya Sewa: "))
    except ValueError:
        print("Biaya sewa harus berupa angka!")
        return

    for item in buku:
        if item["ID Buku"] == ID_buku:
            print("ID Buku sudah ada!")
            return
    
    buku.append({
        "ID Buku": ID_buku,
        "Judul Buku": Judul_buku,
        "Pengarang": Pengarang,
        "Biaya Sewa": Biaya_sewa
    })
    
    if SimpanDataBuku(buku):
        print("Buku berhasil ditambahkan!")
    else:
        print("Gagal menambahkan buku!")

def tampilkan_buku_admin():
    buku = BacaDataBuku()
    
    if not buku:
        print("Belum ada buku dalam sistem.")
        return
    
    tabel = PrettyTable()
    tabel.title = "Daftar Buku"
    tabel.field_names = ["ID Buku", "Judul Buku", "Pengarang", "Biaya Sewa"]
    
    for item in buku:
        tabel.add_row([
            item["ID Buku"],
            item["Judul Buku"], 
            item["Pengarang"],
            item["Biaya Sewa"]
        ])
    
    print(tabel)

def ubah_buku():
    buku = BacaDataBuku()
    
    if not buku:
        print("Belum ada buku dalam sistem.")
        return
    
    tampilkan_buku_admin()
    ID_buku = input("Masukkan ID Buku yang ingin diubah: ")
    
    for item in buku:
        if item["ID Buku"] == ID_buku:
            print(f"Mengubah buku: {item['Judul Buku']}")
            
            Judul_buku_baru = input("Masukkan Judul Buku baru: ")
            Pengarang_baru = input("Masukkan Pengarang baru: ")
            
            try:
                Biaya_sewa_baru = int(input("Masukkan Biaya Sewa baru: "))
            except ValueError:
                print("Biaya sewa harus berupa angka!")
                return
            
            item["Judul Buku"] = Judul_buku_baru
            item["Pengarang"] = Pengarang_baru
            item["Biaya Sewa"] = Biaya_sewa_baru
            
            if SimpanDataBuku(buku):
                print("Buku berhasil diubah!")
            else:
                print("Gagal mengubah buku!")
            return
    
    print("ID Buku tidak ditemukan!")

def hapus_buku():
    buku = BacaDataBuku()
    
    if not buku:
        print("Belum ada buku dalam sistem.")
        return
    
    tampilkan_buku_admin()
    id_buku = input("Masukkan ID Buku yang ingin dihapus: ")
    
    for i, item in enumerate(buku):
        if item["ID Buku"] == id_buku:
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus buku '{item['Judul Buku']}'? (y/t): ")
            if konfirmasi.lower() == 'y':
                del buku[i]
                if SimpanDataBuku(buku):
                    print("Buku berhasil dihapus!")
                else:
                    print("Gagal menghapus buku!")
                return
            else:
                print("Penghapusan dibatalkan.")
                return
    
    print("ID Buku tidak ditemukan!")

def menu_user():
    global logged_in_user
    
    while True:
        print("======== MENU USER ========")
        print("1. Tampilkan Buku")
        print("2. Sewa Buku")
        print("3. Saldo Anda")
        print("4. Logout")
        print("===========================")
        pilihan = input("Pilih menu [1-4]: ")
        
        if pilihan == "1":
            tampilkan_buku_user()
        elif pilihan == "2":
            sewa_buku()
        elif pilihan == "3":
            cek_saldo()
        elif pilihan == "4":
            print("Logout user berhasil.")
            logged_in_user = None
            break
        else:
            print("Pilihan tidak valid!")

def tampilkan_buku_user():
    buku = BacaDataBuku()
    
    if not buku:
        print("Belum ada buku dalam sistem.")
        return
    
    tabel = PrettyTable()
    tabel.title = "Daftar Buku Tersedia"
    tabel.field_names = ["ID Buku", "Judul Buku", "Pengarang", "Biaya Sewa"]
    
    for item in buku:
        tabel.add_row([
            item["ID Buku"],
            item["Judul Buku"],
            item["Pengarang"],
            item["Biaya Sewa"]
        ])
    
    print(tabel)

def sewa_buku():
    global logged_in_user
    
    if not logged_in_user:
        print("Anda belum login!")
        return
    
    buku = BacaDataBuku()
    data_akun = BacaDataAkun()
    
    if not buku:
        print("Belum ada buku dalam sistem.")
        return
    
    tampilkan_buku_user()
    id_buku = input("Masukkan ID Buku yang ingin disewa: ")
    
    buku_dipilih = None
    for item in buku:
        if item["ID Buku"] == id_buku:
            buku_dipilih = item
            break
    
    if not buku_dipilih:
        print("ID Buku tidak ditemukan!")
        return
    
    akun_user = None
    for akun in data_akun:
        if akun["username"] == logged_in_user:
            akun_user = akun
            break
    
    if not akun_user:
        print("Data akun tidak ditemukan!")
        return
    
    print("==========================================================")
    print("invoice penyewaan buku")
    print("\nID Buku: {}" \
        "\nJudul Buku: {}" \
        "\nPengarang: {}" \
        "\nBiaya Sewa: Rp. {}" \
        .format(buku_dipilih["ID Buku"], buku_dipilih["Judul Buku"], buku_dipilih["Pengarang"], buku_dipilih["Biaya Sewa"]))
    print("==========================================================")
    print("Silakan lakukan pembayaran sebesar Rp. {}".format(buku_dipilih["Biaya Sewa"]))
    
    konfirmasi = input("Tekan y/t untuk konfirmasi pembayaran: ").lower()
    
    if konfirmasi == "y":
        saldo_user = akun_user["saldo"]
        biaya_sewa = buku_dipilih["Biaya Sewa"]
        
        if saldo_user >= biaya_sewa:
            akun_user["saldo"] = saldo_user - biaya_sewa
            waktu_sekarang = time.time()
            batas_waktu = waktu_sekarang + (7 * 24 * 60 * 60)
            batas_tanggal = time.strftime('%d-%m-%Y', time.localtime(batas_waktu))
            
            if SimpanDataAkun(data_akun):
                print("Pembayaran berhasil! Buku '{}' telah disewa.".format(buku_dipilih["Judul Buku"]))
                print("Batas waktu sewa: {}".format(batas_tanggal))
            else:
                print("Gagal menyimpan data pembayaran!")
        else:
            print("Saldo tidak cukup!")
    else:
        print("Pembayaran dibatalkan.")

def cek_saldo():
    global logged_in_user
    
    if not logged_in_user:
        print("Anda belum login!")
        return
    
    data_akun = BacaDataAkun()
    
    for akun in data_akun:
        if akun["username"] == logged_in_user:
            print("Saldo Anda saat ini adalah", akun["saldo"])
            return
    
    print("Data akun tidak ditemukan!")

menu_utama()