def hitung_karakter(text):
    vokal = "aiueoAIUEO"
    jumlah_vokal = 0
    jumlah_konsonan = 0
    for char in text:
        if char.isalpha():
            if char in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1
    jumlah_kata = len(text.split())
    return jumlah_vokal, jumlah_konsonan, jumlah_kata

kalimat = input("Masukkan kalimat: ")
vokal, konsonan, kata = hitung_karakter(kalimat)
print(f"Jumlah huruf vokal: {vokal}")
print(f"Jumlah huruf konsonan: {konsonan}")
print(f"Jumlah kata: {kata}")
