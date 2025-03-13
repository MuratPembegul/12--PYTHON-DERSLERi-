# Bir liste oluşturuyoruz
meyveler = ["elma", "muz", "çilek", "portakal"]

# Listenin ilk elemanını ekrana yazdırıyoruz
print(meyveler[0])  # "elma" çıktısı

# Listenin uzunluğunu buluyoruz
print(len(meyveler))  # 4 çıktısı

# Listeye yeni bir eleman ekliyoruz
meyveler.append("kavun")
print(meyveler)  # ["elma", "muz", "çilek", "portakal", "kavun"]

# Listenin belirli bir elemanını siliyoruz
meyveler.remove("çilek")
print(meyveler)  # ["elma", "muz", "portakal", "kavun"]

# Listedeki elemanları sırayla yazdırmak için for döngüsü kullanıyoruz
for meyve in meyveler:
    print(meyve)
