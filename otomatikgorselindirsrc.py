import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from zipfile import ZipFile

# ✅ Dosya isimleri
file_names = [
    "1-Character Traits-Human.png",
    "2-Character Traits-Child.png",
    "3-Character Traits-Teenager.png",
    "4-Character Traits-Adult.png",
    "5-Character Traits-Elderly.png",
    "6-Character Traits-Animal.png",
    "7-Character Traits-Cute Animal.png",
    "8-Character Traits-Wild Beast.png",
    "9-Character Traits-Anthropomorphic Animal.png",
    "10-Character Traits-Elf (Elf).png",
    "11-Character Traits-Fairy.png",
    "12-Character Traits-Dwarf.png",
    "13-Character Traits-Orc (Orc).png",
    "14-Character Traits-Goblin (Goblin).png",
    "15-Character Traits-Dragon.png",
    "16-Character Traits-Phoenix.png",
    "17-Character Traits-Mermaid.png",
    "18-Character Traits-Centaur (Centaur).png"
]

# 🌐 Chrome başlat
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# ChatGPT konuşma sayfasını aç
driver.get("https://chatgpt.com/c/681baf35-9b70-8001-8b27-b25815929fcc")  # Buraya senin ilgili konuşma URL'ini yapıştırmalısın

# Bekle (yüklemesi uzun sürebilir)
time.sleep(10)

# Görsel URL'lerini çek
images = driver.find_elements(By.TAG_NAME, "img")
openai_img_urls = [img.get_attribute("src") for img in images if img.get_attribute("src") and "sdmntprcentralus.oaiusercontent.com/files" in img.get_attribute("src")]

# 📂 Kayıt klasörü
os.makedirs("yakalanan_gorseller", exist_ok=True)

# Görselleri sırayla indir ve yeniden adlandır
for idx, (url, name) in enumerate(zip(openai_img_urls, file_names)):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open(f"yakalanan_gorseller/{name}", "wb") as f:
                f.write(r.content)
            print(f"✅ İndirildi: {name}")
        else:
            print(f"⚠️ Hata: {url}")
    except Exception as e:
        print(f"❌ İndirme hatası ({url}):", e)

# Zip oluştur
with ZipFile("All-Character-Traits-from-img.zip", 'w') as zipf:
    for name in file_names:
        path = f"yakalanan_gorseller/{name}"
        if os.path.exists(path):
            zipf.write(path, arcname=name)

print("🎉 ZIP tamamlandı: All-Character-Traits-from-img.zip")

driver.quit()
