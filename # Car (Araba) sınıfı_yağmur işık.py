# Car (Araba) sınıfı
class Car:
    def __init__(self, marka, model, renk, max_hiz):
        """Araba sınıfının yapıcı metodu (constructor)."""
        self.marka = marka        # Araba markası
        self.model = model        # Araba modeli
        self.renk = renk          # Araba rengi
        self.max_hiz = max_hiz    # Arabanın maksimum hızı
        self.hiz = 0              # Başlangıçta hız sıfırdır (durağan)

    def hizlan(self, artis_miktari):
        """Arabanın hızını arttırma metodu."""
        if self.hiz + artis_miktari > self.max_hiz:
            self.hiz = self.max_hiz  # Hızı maksimum hızdan fazla yapma
        else:
            self.hiz += artis_miktari
        print(f"Araba hızlandı! Şu anki hız: {self.hiz} km/h")

    def fren(self):
        """Araba fren yapma metodu."""
        if self.hiz == 0:
            print("Araba zaten duruyor.")
        else:
            self.hiz = 0
            print("Araba durdu!")

    def hiz_goster(self):
        """Arabanın mevcut hızını gösterme metodu."""
        print(f"Mevcut hız: {self.hiz} km/h")

    def bilgileri_yazdir(self):
        """Arabanın tüm bilgilerini yazdıran metot."""
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Renk: {self.renk}")
        print(f"Max Hız: {self.max_hiz} km/h")
        print(f"Mevcut Hız: {self.hiz} km/h")


# Örnek kullanım
if __name__ == "__main__":
    # Yeni bir araba nesnesi oluşturma
    araba1 = Car("Toyota", "Corolla", "Beyaz", 180)
    
    # Araba bilgilerini yazdırma
    araba1.bilgileri_yazdir()
    
    # Hızlanma
    araba1.hizlan(50)
    araba1.hizlan(80)
    araba1.hizlan(100)  # Bu hız max_hiz'ı aşmamalı
    
    # Mevcut hızı gösterme
    araba1.hiz_goster()
    
    # Fren yapma
    araba1.fren()
    araba1.hiz_goster()  # Araba durduktan sonra hız sıfırlanacak
