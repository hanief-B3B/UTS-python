# Praktikum Python - Soal 7 s.d. 10

Dokumen ini menjelaskan singkat masing-masing program dan menyertakan hasil outputnya.

---

## Soal 7

### Deskripsi
Fungsi `kategori_usia(usia)` digunakan untuk menentukan kategori usia seseorang:
- `< 12` → Anak-anak
- `12–17` → Remaja
- `18–59` → Dewasa
- `>= 60` → Lansia

### Output
![Output Soal 7](https://cdn.discordapp.com/attachments/1335953538785742869/1365368417036800010/Screenshot_From_2025-04-25_17-42-41.png?ex=680d0ded&is=680bbc6d&hm=0fec31d82dfa698d307d4547c85c0f19acbfbef602d3eba0c074913c1be94b2e)

---

## Soal 8

### Deskripsi
Fungsi `analisis_kalimat(kalimat)` menghitung:
- Jumlah huruf vokal (`a`, `i`, `u`, `e`, `o`)
- Jumlah huruf konsonan
- Total huruf dalam kalimat

### Output
![Output Soal 8](https://cdn.discordapp.com/attachments/1335953538785742869/1365368417733050540/Screenshot_From_2025-04-25_17-43-09.png?ex=680d0dee&is=680bbc6e&hm=63f58fa6d3d57b157d8107f2afd971b783527140d6eb8841f5e92c52698be416)

---

## Soal 9

### Deskripsi
Fungsi `analisis_transaksi(data)` akan:
- Menjumlahkan seluruh transaksi (saldo akhir)
- Menentukan hari dengan transaksi terbesar
- Menemukan hari tanpa transaksi

### Output
![Output Soal 9](https://media.discordapp.net/attachments/1335953538785742869/1365366746135003196/Screenshot_From_2025-04-25_17-28-31.png?ex=680d0c5f&is=680bbadf&hm=1dd1175a8dd122bb967465836300b99b834d6699aa8c670033a4c8320ec791ee&=&format=webp&quality=lossless&width=1542&height=867)

---

## Soal 10

### Deskripsi
Program interaktif dengan fitur:
- Menambah tugas
- Mengubah status tugas
- Menampilkan semua tugas

### Output (cuplikan interaksi di terminal)
```
$ python jawaban-no-10.py 

Menu To-Do List:
1. Tambah tugas baru
2. Ubah status tugas
3. Tampilkan semua tugas
4. Keluar
Pilih menu (1-4): 3

Daftar Tugas:
1. Belajar Python - Status: Belum
2. Cuci baju - Status: Sudah

Menu To-Do List:
1. Tambah tugas baru
2. Ubah status tugas
3. Tampilkan semua tugas
4. Keluar
Pilih menu (1-4): 1
Masukkan nama tugas baru: UTS
Tugas berhasil ditambahkan!

Menu To-Do List:
1. Tambah tugas baru
2. Ubah status tugas
3. Tampilkan semua tugas
4. Keluar
Pilih menu (1-4): 3

Daftar Tugas:
1. Belajar Python - Status: Belum
2. Cuci baju - Status: Sudah
3. UTS - Status: Belum

Menu To-Do List:
1. Tambah tugas baru
2. Ubah status tugas
3. Tampilkan semua tugas
4. Keluar
Pilih menu (1-4): 2

Daftar Tugas:
1. Belajar Python - Status: Belum
2. Cuci baju - Status: Sudah
3. UTS - Status: Belum
Pilih nomor tugas yang akan diubah statusnya: 3
Status berhasil diubah!

Menu To-Do List:
1. Tambah tugas baru
2. Ubah status tugas
3. Tampilkan semua tugas
4. Keluar
Pilih menu (1-4): 3

Daftar Tugas:
1. Belajar Python - Status: Belum
2. Cuci baju - Status: Sudah
3. UTS - Status: Sudah

Menu To-Do List:
1. Tambah tugas baru
2. Ubah status tugas
3. Tampilkan semua tugas
4. Keluar
Pilih menu (1-4): 4
Program selesai.
```
