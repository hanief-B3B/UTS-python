def kategori_usia(usia):
    if usia < 12:
        return "Anak-anak"
    elif usia < 18:
        return "Remaja"
    elif usia < 60:
        return "Dewasa"
    else:
        return "Lansia"

# Contoh penggunaan
print(kategori_usia(10))  # Output: Anak-anak
print(kategori_usia(15))  # Output: Remaja
print(kategori_usia(30))  # Output: Dewasa
print(kategori_usia(65))  # Output: Lansia
