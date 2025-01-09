#  Person sınıfı
class Person:
    def __init__(self, ad, yas, adres):
        self.ad = ad
        self.yas = yas
        self.adres = adres

    def yas_hesapla(self, dogum_yili):
        """Yaş hesaplama fonksiyonu"""
        current_year = 2024
        self.yas = current_year - dogum_yili
        return self.yas

    def bilgiler(self):
        """Temel bilgileri döndüren metot"""
        return f"Ad: {self.ad}, Yaş: {self.yas}, Adres: {self.adres}"

    def bilgileri_yazdir(self):
        """Bilgileri yazdıran metot"""
        print(self.bilgiler())


# Student sınıfı, Person sınıfından türetiliyor
class Student(Person):
    def __init__(self, ad, yas, adres, ogrenci_no):
        super().__init__(ad, yas, adres)  # Person sınıfının __init__ metodunu çağırır
        self.ogrenci_no = ogrenci_no
        self.dersler = []  # Ders listesi
        self.notlar = {}   # Derslere ait notlar

    def ders_ekle(self, ders_adi):
        """Öğrenciye ders ekleyen metot"""
        self.dersler.append(ders_adi)

    def not_ekle(self, ders_adi, not_degeri):
        """Öğrencinin ders notunu ekleyen metot"""
        if ders_adi in self.dersler:
            self.notlar[ders_adi] = not_degeri
        else:
            print(f"{ders_adi} dersi, öğrenciye ait değil.")

    def ortalama_hesapla(self):
        """Öğrencinin ders notlarının ortalamasını hesaplar"""
        if not self.notlar:
            return 0
        return sum(self.notlar.values()) / len(self.notlar)

    def bilgiler(self):
        """Öğrenci bilgilerini döndüren metot"""
        dersler_str = ', '.join(self.dersler) if self.dersler else "Hiç ders alınmadı"
        notlar_str = ', '.join([f"{ders}: {not_}°" for ders, not_ in self.notlar.items()]) if self.notlar else "Notlar girilmedi"
        return f"{super().bilgiler()}, Öğrenci No: {self.ogrenci_no}, Dersler: {dersler_str}, Notlar: {notlar_str}"


# Teacher sınıfı, Person sınıfından türetiliyor
class Teacher(Person):
    def __init__(self, ad, yas, adres, brans):
        super().__init__(ad, yas, adres)
        self.brans = brans
        self.dersler = []  # Öğretmenin verdiği dersler

    def ders_ekle(self, ders_adi):
        """Öğretmene ders ekleyen metot"""
        self.dersler.append(ders_adi)

    def dersler_goster(self):
        """Öğretmenin verdiği dersleri gösteren metot"""
        return ', '.join(self.dersler) if self.dersler else "Hiç ders verilmedi"

    def bilgiler(self):
        """Öğretmen bilgilerini döndüren metot"""
        return f"{super().bilgiler()}, Branş: {self.brans}, Verilen Dersler: {self.dersler_goster()}"


# Örnek kullanım
if __name__ == "__main__":
    # Person örneği
    kisi = Person("Ahmet", 35, "İstanbul")
    kisi.yas_hesapla(1989)  # Yaş hesapla
    kisi.bilgileri_yazdir()

    # Student örneği
    ogrenci = Student("Ali", 20, "Ankara", "12345")
    ogrenci.ders_ekle("Matematik")
    ogrenci.ders_ekle("Fizik")
    ogrenci.not_ekle("Matematik", 85)
    ogrenci.not_ekle("Fizik", 90)
    print(ogrenci.bilgiler())
    print(f"Öğrencinin Ortalama Notu: {ogrenci.ortalama_hesapla():.2f}")

    # Teacher örneği
    ogretmen = Teacher("Ayşe", 40, "İzmir", "Matematik")
    ogretmen.ders_ekle("Matematik")
    ogretmen.ders_ekle("Geometri")
    print(ogretmen.bilgiler())
