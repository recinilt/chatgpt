import pyautogui
import time
import json
import os
import keyboard

islemler = []

def koordinat_al():
    print("📍 Lütfen mouse'u istediğin yere getir ve 5 saniye bekle...")
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"✅ Alınan koordinatlar: {x}, {y}")
    return x, y

def float_input(soru):
    while True:
        cevap = input(soru).strip()
        try:
            return float(cevap)
        except ValueError:
            print("⚠️ Lütfen geçerli bir sayı girin. Örneğin: 1, 2.5, 0.7")

def int_input(soru):
    while True:
        cevap = input(soru).strip()
        if cevap.isdigit():
            return int(cevap)
        print("⚠️ Lütfen geçerli bir tamsayı girin.")

def islem_ekle():
    while True:
        print("\n🔧 Yeni işlem seç:")
        print("1 - Mouse tıklaması")
        print("2 - Yazı yazma")
        print("3 - Enter tuşuna basma")
        print("4 - Bekleme (sadece bekle)")
        print("5 - İşlem eklemeyi bitir (çık)")
        print("6 - Tuş kombinasyonu (hazır veya canlı basış)")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            x, y = koordinat_al()
            bekle = float_input("Bu tıklamadan sonra kaç saniye beklensin?: ")
            islemler.append({
                "tur": "click",
                "x": x,
                "y": y,
                "bekle": bekle
            })

        elif secim == "2":
            yazi = input("Yazılacak metni girin: ")
            bekle = float_input("Bu yazmadan sonra kaç saniye beklensin?: ")
            islemler.append({
                "tur": "yaz",
                "metin": yazi,
                "bekle": bekle
            })

        elif secim == "3":
            bekle = float_input("Enter işleminden sonra kaç saniye beklensin?: ")
            islemler.append({
                "tur": "enter",
                "bekle": bekle
            })

        elif secim == "4":
            bekle = float_input("Kaç saniye sadece beklesin?: ")
            islemler.append({
                "tur": "bekle",
                "bekle": bekle
            })

        elif secim == "6":
            print("\n🔢 Hazır tuş kombinasyonlarından birini seç:")
            hazir_kombinasyonlar = [
                "ctrl+a", "ctrl+c", "ctrl+v", "ctrl+z", "ctrl+s",
                "tab", "esc", "enter",
                "up", "down", "left", "right",
                "alt+tab"
            ]

            for i, kombo in enumerate(hazir_kombinasyonlar, 1):
                print(f"{i}. {kombo}")
            print(f"{len(hazir_kombinasyonlar)+1}. Diğer (kendim basacağım)")

            secim_kombo = input("➡️ Numara girin: ").strip()
            if secim_kombo.isdigit():
                secim_kombo = int(secim_kombo)
                if 1 <= secim_kombo <= len(hazir_kombinasyonlar):
                    kombinasyon_str = hazir_kombinasyonlar[secim_kombo - 1]
                elif secim_kombo == len(hazir_kombinasyonlar) + 1:
                    print("⏱️ Şimdi tuş kombinasyonunu bas. 3 saniyen var...")
                    keyboard.start_recording()
                    time.sleep(3)
                    events = keyboard.stop_recording()
                    combo = []
                    for e in events:
                        if e.event_type == "down" and e.name not in combo:
                            combo.append(e.name)
                    if not combo:
                        print("⚠️ Geçerli tuş kombinasyonu algılanmadı.")
                        continue
                    if "ctrl" in combo and "c" in combo:
                        print("⚠️ 'ctrl+c' kombinasyonu sistemde çıkışı tetikler, kullanılamaz.")
                        continue
                    kombinasyon_str = "+".join(combo)
                else:
                    print("⚠️ Geçerli bir seçim yapılmadı.")
                    continue
            else:
                print("⚠️ Sayı girmelisin.")
                continue

            tekrar = int_input(f"'{kombinasyon_str}' kaç kez basılsın?: ")
            bekle = float_input(f"'{kombinasyon_str}' kombinasyonundan sonra kaç saniye beklensin?: ")

            islemler.append({
                "tur": "kombinasyon",
                "kombinasyon": kombinasyon_str,
                "tekrar": tekrar,
                "bekle": bekle
            })
            print(f"✅ Eklendi: {kombinasyon_str} x{tekrar}")

        elif secim == "5":
            break
        else:
            print("⚠️ Geçersiz seçim. Tekrar deneyin.")

def islemleri_kaydet():
    ayar_adi = input("💾 Bu ayarı hangi isimle kaydetmek istersin?: ").strip()
    dosya_adi = f"ayarlar/{ayar_adi}.json"
    os.makedirs("ayarlar", exist_ok=True)
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(islemler, f, indent=4, ensure_ascii=False)
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
    secim = input("➡️ Yüklemek istediğin ayarın numarasını yaz: ").strip()
    if not secim.isdigit() or int(secim) < 1 or int(secim) > len(dosyalar):
        print("⚠️ Geçerli bir numara girilmedi.")
        return False
    secilen = dosyalar[int(secim) - 1]
    with open(f"ayarlar/{secilen}", "r", encoding="utf-8") as f:
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
                keyboard.write(islem["metin"])
            elif islem["tur"] == "enter":
                pyautogui.press("enter")
            elif islem["tur"] == "kombinasyon":
                try:
                    for _ in range(islem.get("tekrar", 1)):
                        keyboard.press_and_release(islem["kombinasyon"])
                        time.sleep(0.05)
                except Exception as e:
                    print(f"⚠️ Tuş kombinasyonu gönderilemedi: {e}")
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
