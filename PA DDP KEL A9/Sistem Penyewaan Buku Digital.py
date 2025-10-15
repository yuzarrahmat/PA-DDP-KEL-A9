import json
from prettytable import PrettyTable
import os

def menu_awal():
    while True:
        print("======== MENU UTAMA ========")
        print("1. Login User")
        print("2. Register User")
        print("3. Login Admin")
        print("4. Keluar")
        print("==========================")
        pilihan = input("Pilih menu [1-4]: ")
        if pilihan == "1":
            Login_User()
        elif pilihan == "2":
            Register_User()
        elif pilihan == "3":
            login_admin()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

def DataBuku():
    with open('PA DDP KEL A9/Buku.json', 'r') as file:
        buku = json.load(file)
        tabel = PrettyTable()
        tabel.title = "Daftar Buku"
        tabel.field_names =["ID Buku", "Judul Buku", "Pengarang"] 
        for item in buku:
            tabel.add_row([item["ID Buku"], item["Judul Buku"], item["Pengarang"]])
    return buku

def DataAkun():
    with open('PA DDP KEL A9/Akun User.json', 'r') as file:
        akun = json.load(file)
    return akun

def Login_User():
    akun = DataAkun()
    email = input("Masukkan e mail: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for user in akun:
        if user["e mail"] == email and user["username"] == username and user["password"] == password:
            print("Login berhasil!")
            main()
    print("Login gagal! Periksa kembali e mail, username, dan password Anda.")
    return False

def Register_User():
    akun = DataAkun()
    email = input("Masukkan e mail: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    akun.append({"e mail": email, "username": username, "password": password})
    with open('PA DDP KEL A9/Akun User.json', 'w') as file:
        json.dump(akun, file, indent=4)
    print("Registrasi berhasil! Silakan login dengan akun baru Anda.")
    return

def login_admin():
    admin_username = "admin"
    admin_password = "admin123"
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username == admin_username and password == admin_password:
        print("Login admin berhasil!")
        menu_admin()
    else:
        print("Login admin gagal! Periksa kembali username dan password Anda.")
        return False

def main():
    while True:
        print("======== MENU SISTEM PENYEWAAN BUKU DIGITAL ========")
        print("1. Tampilkan Buku yang Tersedia")
        print("2. Sewa Buku")
        print("3. Logout")
        print("===================================================")
        pilihan = input("Pilih menu [1-3]: ")
        if pilihan == "1":
            DataBuku()
            buku = DataBuku()
            tabel = PrettyTable()
            tabel.title = "Daftar Buku"
            tabel.field_names = ["ID Buku", "Judul Buku", "Pengarang"]
            for item in buku:
                tabel.add_row([item["ID Buku"], item["Judul Buku"], item["Pengarang"]])
            print(tabel)
        elif pilihan == "2":
            sewa_buku = input("Masukkan ID Buku yang ingin disewa: ")
            buku = DataBuku()
            for item in buku:
                if item["ID Buku"] == sewa_buku:
                    print(f"Buku '{item['Judul Buku']}' berhasil disewa!")
                    buku.remove(item)
                    with open('PA DDP KEL A9/Buku.json', 'w') as file:
                        json.dump(buku, file, indent=4)
                    print("Apakah anda ingin menyewa buku lain? (ya/tidak)")
                    pilihan = input()
                    if pilihan.lower() == "ya":
                        main()
                    elif pilihan.lower() == "tidak":
                        print("Terima kasih telah menggunakan layanan kami.")
                        return
                    else:
                        print("Pilihan tidak valid!")

def menu_admin():
    while True:
        print("======== MENU ADMIN ========")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Ubah Perbukuan")
        print("4. Logout")
        print("===========================")
        pilihan = input("Pilih menu [1-4]: ")
        if pilihan == "1":
            buku = DataBuku()
            id_buku = input("Masukkan ID Buku: ")
            judul_buku = input("Masukkan Judul Buku: ")
            pengarang = input("Masukkan Pengarang: ")
            buku.append({"ID Buku": id_buku, "Judul Buku": judul_buku, "Pengarang": pengarang})
            with open('PA DDP KEL A9/Buku.json', 'w') as file:
                json.dump(buku, file, indent=4)
            print("Buku berhasil ditambahkan!")
        elif pilihan == "2":
            DataBuku()
            menu_admin()
        elif pilihan == "3":
            buku = DataBuku()
            print("1. Ubah Buku")
            print("2. Hapus Buku")
            pilihan = input("Pilih menu [1-2]: ")
            if pilihan == "1":
                id_buku = input("Masukkan ID Buku yang ingin diubah: ")
                for item in buku:
                    if item["ID Buku"] == id_buku:
                        judul_buku = input("Masukkan Judul Buku baru: ")
                        pengarang = input("Masukkan Pengarang baru: ")
                        item["Judul Buku"] = judul_buku
                        item["Pengarang"] = pengarang
                        with open('PA DDP KEL A9/Buku.json', 'w') as file:
                            json.dump(buku, file, indent=4)
                        print("Buku berhasil diubah!")
                        menu_admin()
            if pilihan == "2":
                id_buku = input("Masukkan ID Buku yang ingin dihapus: ")
                for item in buku:
                    if item["ID Buku"] == id_buku:
                        buku.remove(item)
                        with open('PA DDP KEL A9/Buku.json', 'w') as file:
                            json.dump(buku, file, indent=4)
                        print("Buku berhasil dihapus!")
                        menu_admin()
            else:
                print("ID Buku tidak ditemukan!")
                menu_admin()
        elif pilihan == "4":
            print("Logout admin berhasil.")
            menu_awal()
        else:
            print("Pilihan tidak valid!")
menu_awal()