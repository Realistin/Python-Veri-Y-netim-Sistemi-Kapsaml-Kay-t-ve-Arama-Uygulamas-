class DataManager:
    def __init__(self):
        self.data = {"basketbolcular": {}, "sozluk (çeviri)": {}, "firma bilgileri": {}, "kitap bilgileri": {}}

    def add(self, category, key, value):
        if category in self.data:
            self.data[category][key] = value

    def remove(self, category, key):
        if category in self.data and key in self.data[category]:
            del self.data[category][key]
            return True
        return False

    def search(self, category, key):
        if category in self.data:
            for k, v in self.data[category].items():
                if key.lower() in k.lower():
                    return {k: v}
        return "Bulunamadı"

    def update(self, category, key, value):
        if category in self.data and key in self.data[category]:
            self.data[category][key] = value
            return True
        return False

    def display(self, category):
        return self.data[category] if category in self.data else "Kategori bulunamadı."


# Genel Veri Yönetimi
veri = DataManager()

# Örnek Kullanımlar
veri.add("basketbolcular", "Michael Jordan", {"Boy": "2.00m"})
veri.add("basketbolcular", "Lebron James", {"Boy": "2.05m"})
veri.add("sozluk (çeviri)", "apple", "pomme")
veri.add("sozluk (çeviri)", "car", "voiture")
veri.add("firma bilgileri", "Onur PEHLİVAN", {"Telefon": "535-732-24-24", "E-Posta": "opehlivan@firma.com", "Pozisyon": "Kurucu"})
veri.add("kitap bilgileri", "1984", {"Yazar": "George Orwell", "Tür": "Distopya", "Yayın Yılı": 1949})

# Kullanıcı Girişiyle Veri Yönetimi
while True:
    print("\n1- Ekleme\n2- Silme\n3- Arama\n4- Güncelleme\n5- Göster\n6- Çıkış")
    secim = input("Seçiminizi yapın: ")

    kategoriler = {"1": "basketbolcular", "2": "sozluk (çeviri)", "3": "firma bilgileri", "4": "kitap bilgileri"}

    if secim in ["1", "2", "3", "4", "5"]:
        print("\n1- Basketbolcular\n2- Sözlük (çeviri)\n3- Firma Bilgileri\n4- Kitap Bilgileri")
        kategori_secim = input("Kategori seçin: ")
        category = kategoriler.get(kategori_secim, None)

        if not category:
            print("Geçersiz kategori.")
            continue

    if secim == "1":
        key = input("Anahtar (ad soyad,  kelime, kitap adı, vb.): ")
        value = input("Değer (bilgi, çeviri, açıklama, boy vb.): ")
        veri.add(category, key, value)
    elif secim == "2":
        key = input("Silinecek anahtar: ")
        if veri.remove(category, key):
            print("Silindi.")
        else:
            print("Anahtar bulunamadı.")
    elif secim == "3":
        key = input("Aranacak anahtar: ")
        print("Sonuç:", veri.search(category, key))
    elif secim == "4":
        key = input("Güncellenecek anahtar: ")
        value = input("Yeni değer: ")
        if veri.update(category, key, value):
            print("Güncellendi.")
        else:
            print("Anahtar bulunamadı.")
    elif secim == "5":
        print("Veriler:", veri.display(category))
    elif secim == "6":
        break
    else:
        print("Geçersiz seçim.")
