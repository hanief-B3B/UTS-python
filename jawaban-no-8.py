def analisis_kalimat(kalimat):
    vokal = {'a', 'i', 'u', 'e', 'o'}
    kalimat_lower = kalimat.lower()
    
    count_vokal = sum(1 for char in kalimat_lower if char in vokal)
    count_konsonan = sum(1 for char in kalimat_lower if char.isalpha() and char not in vokal)
    total_huruf = count_vokal + count_konsonan
    
    print(f"Vokal: {count_vokal}")
    print(f"Konsonan: {count_konsonan}")
    print(f"Total huruf: {total_huruf}")

# Contoh penggunaan
analisis_kalimat("Halo Dunia Python")
