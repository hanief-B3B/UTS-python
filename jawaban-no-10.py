todo = {
    "Belajar Python": "belum",
    "Cuci baju": "selesai"
}

def tambah_tugas(todo_dict):
    tugas = input("Masukkan nama tugas baru: ")
    if tugas in todo_dict:
        print("Tugas sudah ada!")
    else:
        todo_dict[tugas] = "belum"
        print(f"Tugas '{tugas}' berhasil ditambahkan.")

def ubah_status(todo_dict):
    print("\nDaftar Tugas:")
    for tugas, status in todo_dict.items():
        print(f"- {tugas} ({status})")

    tugas = input("\nMasukkan nama tugas yang ingin diubah statusnya: ")
    if tugas not in todo_dict:
        print("Tugas tidak ditemukan!")
        return

    new_status = input("Masukkan status baru (selesai/belum): ").lower()
    if new_status not in ["selesai", "belum"]:
        print("Status tidak valid!")
        return

    todo_dict[tugas] = new_status
    print("Status berhasil diubah!")

def tampilkan_tugas(todo_dict):
    print("\nPilih filter status:")
    print("1. Tampilkan semua")
    print("2. Selesai")
    print("3. Belum")
    pilihan = input("Pilihan (1/2/3): ")

    print("\n=== Daftar Tugas ===")
    if pilihan == '1':
        for tugas, status in todo_dict.items():
            print(f"- {tugas} ({status})")
    elif pilihan == '2':
        for tugas, status in todo_dict.items():
            if status == "selesai":
                print(f"- {tugas} ({status})")
    elif pilihan == '3':
        for tugas, status in todo_dict.items():
            if status == "belum":
                print(f"- {tugas} ({status})")
    else:
        print("Pilihan tidak valid!")

while True:
    print("\n=== Menu To-Do List ===")
    print("1. Tambah Tugas Baru")
    print("2. Ubah Status Tugas")
    print("3. Tampilkan Tugas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == '1':
        tambah_tugas(todo)
    elif pilihan == '2':
        ubah_status(todo)
    elif pilihan == '3':
        tampilkan_tugas(todo)
    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
