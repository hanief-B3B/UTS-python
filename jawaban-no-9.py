transaksi = [("Senin", 50000), ("Selasa", -20000), ("Rabu", 0), ("Kamis", 100000)]

def hitung_saldo(transaksi_list):
    return sum(nominal for hari, nominal in transaksi_list)

def hari_pengeluaran_terbesar(transaksi_list):
    pengeluaran = [(hari, abs(nominal)) for hari, nominal in transaksi_list if nominal < 0]
    if not pengeluaran:
        return "Tidak ada pengeluaran"
    hari_terbesar = max(pengeluaran, key=lambda x: x[1])
    return hari_terbesar[0]

def hari_tanpa_transaksi(transaksi_list):
    return [hari for hari, nominal in transaksi_list if nominal == 0]

saldo_akhir = hitung_saldo(transaksi)
hari_pengeluaran = hari_pengeluaran_terbesar(transaksi)
hari_tanpa = hari_tanpa_transaksi(transaksi)

print(f"Saldo akhir: {saldo_akhir}")
print(f"Hari pengeluaran terbesar: {hari_pengeluaran}")
print(f"Hari tanpa transaksi: {', '.join(hari_tanpa) if hari_tanpa else 'Tidak ada'}")
