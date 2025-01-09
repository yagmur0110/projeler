# BankAccount (Banka Hesabı) sınıfı
class BankAccount:
    def __init__(self, hesap_sahibi, hesap_no, bakiye=0):
        """Banka hesabının yapıcı metodu (constructor)."""
        self.hesap_sahibi = hesap_sahibi    # Hesap sahibinin adı
        self.hesap_no = hesap_no            # Hesap numarası
        self.bakiye = bakiye                # Hesap bakiyesi (varsayılan olarak 0)

    def para_yatir(self, miktar):
        """Hesaba para yatırma metodu."""
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL hesabınıza yatırıldı. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar. Lütfen pozitif bir değer girin.")

    def para_cek(self, miktar):
        """Hesaptan para çekme metodu."""
        if miktar <= 0:
            print("Geçersiz miktar. Lütfen pozitif bir değer girin.")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye. Hesabınızda yeterli para bulunmuyor.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL hesabınızdan çekildi. Güncel bakiye: {self.bakiye} TL")

    def bakiye_goster(self):
        """Hesap bakiyesini gösterme metodu."""
        print(f"{self.hesap_sahibi} adlı kişinin hesabında {self.bakiye} TL bulunmaktadır.")

    def hesap_bilgileri(self):
        """Hesap bilgilerini gösterme metodu."""
        print(f"Hesap Sahibi: {self.hesap_sahibi}")
        print(f"Hesap Numarası: {self.hesap_no}")
        print(f"Güncel Bakiye: {self.bakiye} TL")


# Örnek kullanım
if __name__ == "__main__":
    # Yeni bir banka hesabı oluşturma
    hesap1 = BankAccount("Ahmet Yılmaz", "1234567890", 1000)  # 1000 TL başlangıç bakiyesi ile

    # Hesap bilgilerini yazdırma
    hesap1.hesap_bilgileri()

    # Para yatırma
    hesap1.para_yatir(500)

    # Para çekme
    hesap1.para_cek(200)

    # Bakiye görüntüleme
    hesap1.bakiye_goster()

    # Yetersiz bakiye durumu
    hesap1.para_cek(1500)

    # Geçersiz para çekme miktarı
    hesap1.para_cek(-50)
