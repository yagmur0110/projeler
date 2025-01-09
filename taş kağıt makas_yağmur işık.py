import random

def secim_yap():
    """Kullanıcıdan seçim alır (Taş, Kağıt, Makas)."""
    secim = input("Taş, Kağıt, veya Makas seçin (çıkmak için 'çıkış' yazın): ").lower()
    while secim not in ['taş', 'kağıt', 'makas', 'çıkış']:
        secim = input("Geçersiz seçim! Lütfen Taş, Kağıt veya Makas seçin (çıkmak için 'çıkış' yazın): ").lower()
    return secim

def bilgisayar_secimi():
    """Bilgisayar rastgele seçim yapar (Taş, Kağıt, Makas)."""
    return random.choice(['taş', 'kağıt', 'makas'])

def sonucu_belirle(kullanici, bilgisayar):
    """Oyunun sonucunu belirler."""
    if kullanici == bilgisayar:
        return "Beraberlik! İkisi de aynı seçimi yaptı.", 0
    elif (kullanici == 'taş' and bilgisayar == 'makas') or \
         (kullanici == 'kağıt' and bilgisayar == 'taş') or \
         (kullanici == 'makas' and bilgisayar == 'kağıt'):
        return "Kazandınız!", 1
    else:
        return "Kaybettiniz!", -1

def oyun():
    """Oyunun ana fonksiyonu."""
    oyuncu_skoru = 0
    bilgisayar_skoru = 0

    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    
    while True:
        kullanici_secimi = secim_yap()
        if kullanici_secimi == 'çıkış':
            print("Oyunu sonlandırıyorsunuz. Görüşmek üzere!")
            break
        
        bilgisayar_sec = bilgisayar_secimi()
        print(f"Bilgisayarın seçimi: {bilgisayar_sec}")
        
        sonuc, skor = sonucu_belirle(kullanici_secimi, bilgisayar_sec)
        print(sonuc)

        # Skorları güncelleme
        if skor == 1:
            oyuncu_skoru += 1
        elif skor == -1:
            bilgisayar_skoru += 1

        # Skor durumunu yazdırma
        print(f"Skor: Oyuncu {oyuncu_skoru} - {bilgisayar_skoru} Bilgisayar")
        print("-" * 30)

# Oyun başlatma
if __name__ == "__main__":
    oyun()
