import pyautogui
import time
import json
import os
import keyboard  # Türkçe karakter desteği için


islemler = []

def koordinat_al():
    print("📍 Lütfen mouse'u istediğin yere getir ve 5 saniye bekle...")
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"✅ Alınan koordinatlar: {x}, {y}")
    return x, y

def islem_ekle():
    while True:
        print("\n🔧 Yeni işlem seç:")
        print("1 - Mouse tıklaması")
        print("2 - Yazı yazma")
        print("3 - Enter tuşuna basma")
        print("4 - Bekleme (sadece bekle)")
        print("5 - İşlem eklemeyi bitir (çık)")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            x, y = koordinat_al()
            bekle = float(input("Bu tıklamadan sonra kaç saniye beklensin?: "))
            islemler.append({
                "tur": "click",
                "x": x,
                "y": y,
                "bekle": bekle
            })
        elif secim == "2":
            yazi = input("Yazılacak metni girin: ")
            bekle = float(input("Bu yazmadan sonra kaç saniye beklensin?: "))
            islemler.append({
                "tur": "yaz",
                "metin": yazi,
                "bekle": bekle
            })
        elif secim == "3":
            bekle = float(input("Enter işleminden sonra kaç saniye beklensin?: "))
            islemler.append({
                "tur": "enter",
                "bekle": bekle
            })
        elif secim == "4":
            bekle = float(input("Kaç saniye sadece beklesin?: "))
            islemler.append({
                "tur": "bekle",
                "bekle": bekle
            })
        elif secim == "5":
            break
        else:
            print("⚠️ Geçersiz seçim. Tekrar deneyin.")

def islemleri_kaydet():
    ayar_adi = input("💾 Bu ayarı hangi isimle kaydetmek istersin?: ").strip()
    dosya_adi = f"ayarlar/{ayar_adi}.json"
    os.makedirs("ayarlar", exist_ok=True)
    with open(dosya_adi, "w") as f:
        json.dump(islemler, f, indent=4)
    print(f"✅ Ayarlar '{dosya_adi}' dosyasına kaydedildi.")

def kayitli_ayarlari_listele():
    os.makedirs("ayarlar", exist_ok=True)
    dosyalar = [f for f in os.listdir("ayarlar") if f.endswith(".json")]
    if not dosyalar:
        print("📂 Kayıtlı ayar bulunamadı.")
        return None
    print("\n📁 Kayıtlı Ayarlar:")
    for i, dosya in enumerate(dosyalar):
        print(f"{i+1}. {dosya[:-5]}")
    return dosyalar

def ayar_sec_ve_yukle():
    dosyalar = kayitli_ayarlari_listele()
    if not dosyalar:
        return False
    secim = int(input("➡️ Yüklemek istediğin ayarın numarasını yaz: "))
    secilen = dosyalar[secim - 1]
    with open(f"ayarlar/{secilen}", "r") as f:
        global islemler
        islemler = json.load(f)
    print(f"✅ '{secilen}' ayarı yüklendi.")
    return True

def islemleri_baslat():
    print("🚀 İşlemler başlatılıyor. (Sonsuz döngü — Çıkmak için Ctrl+C)")
    while True:
        for i, islem in enumerate(islemler):
            print(f"\n🔁 {i+1}. İşlem: {islem['tur']}")
            if islem["tur"] == "click":
                pyautogui.click(islem["x"], islem["y"])
            elif islem["tur"] == "yaz":
                #pyautogui.write(islem["metin"], interval=0.05)
                keyboard.write(islem["metin"])

            elif islem["tur"] == "enter":
                pyautogui.press("enter")
            elif islem["tur"] == "bekle":
                pass
            time.sleep(islem["bekle"])
            print(f"✅ Beklendi: {islem['bekle']} sn")

def main():
    print("🎛️ Otomasyon Programına Hoş Geldiniz")
    print("1 - Yeni işlem oluştur")
    print("2 - Kayıtlı ayarı yükle")
    secim = input("Seçiminiz: ")

    if secim == "1":
        islem_ekle()
        islemleri_kaydet()
    elif secim == "2":
        basarili = ayar_sec_ve_yukle()
        if not basarili:
            return
    else:
        print("⚠️ Geçersiz seçim.")
        return

    input("🎬 Başlamak için ENTER'a basın...")
    try:
        islemleri_baslat()
    except KeyboardInterrupt:
        print("\n🛑 Otomasyon durduruldu.")

if __name__ == "__main__":
    main()
