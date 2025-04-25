todo_list = {
    "Tugas": [
        {"nama": "Belajar Python", "status": "Belum"},
        {"nama": "Cuci baju", "status": "Sudah"}
    ]
}

def tampilkan_tugas():
    print("\nDaftar Tugas:")
    for i, tugas in enumerate(todo_list["Tugas"], 1):
        print(f"{i}. {tugas['nama']} - Status: {tugas['status']}")

def tambah_tugas():
    nama = input("Masukkan nama tugas baru: ")
    todo_list["Tugas"].append({"nama": nama, "status": "Belum"})
    print("Tugas berhasil ditambahkan!")

def ubah_status():
    tampilkan_tugas()
    try:
        index = int(input("Pilih nomor tugas yang akan diubah statusnya: ")) - 1
        if 0 <= index < len(todo_list["Tugas"]):
            tugas = todo_list["Tugas"][index]
            tugas["status"] = "Sudah" if tugas["status"] == "Belum" else "Belum"
            print("Status berhasil diubah!")
        else:
            print("Nomor tugas tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

while True:
    print("\nMenu To-Do List:")
    print("1. Tambah tugas baru")
    print("2. Ubah status tugas")
    print("3. Tampilkan semua tugas")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        ubah_status()
    elif pilihan == "3":
        tampilkan_tugas()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
