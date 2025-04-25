transaksi = [
    ("Senin", 2000, 1000, 4000, 3000),
    ("Selasa", 0),
    ("Rabu", 10000)
]

def analisis_transaksi(data):
    saldo_akhir = sum(sum(hari[1:]) for hari in data)
    hari_terbesar = max(data, key=lambda x: sum(x[1:]))[0]
    hari_tanpa_transaksi = [hari[0] for hari in data if sum(hari[1:]) == 0]
    
    print(f"Saldo akhir: {saldo_akhir}")
    print(f"Hari pengeluaran terbesar: {hari_terbesar}")
    print(f"Hari tanpa transaksi: {hari_tanpa_transaksi[0] if hari_tanpa_transaksi else 'Tidak ada'}")

analisis_transaksi(transaksi)
