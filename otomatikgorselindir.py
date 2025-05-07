import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from zipfile import ZipFile

# 🔢 Beklenen dosya adları
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

# 🌐 Tarayıcı ayarları
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

# 👇 ChatGPT oturumunun açık olduğu sayfanın URL'sini buraya gir:
driver.get("https://chat.openai.com")  # Gerekirse değiştirilir

# ⏳ Sayfanın tamamen yüklenmesini bekle
time.sleep(10)

# 🖼️ Görselleri bul
images = driver.find_elements(By.TAG_NAME, "img")
image_urls = [img.get_attribute('src') for img in images if img.get_attribute('src') and 'sandbox:/mnt/data/' in img.get_attribute('src')]

# 🎯 Hedef klasör
os.makedirs("chatgpt_gorselleri", exist_ok=True)

# ⬇️ İndir ve yeniden adlandır
for idx, (url, name) in enumerate(zip(image_urls, file_names)):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"chatgpt_gorselleri/{name}", "wb") as f:
                f.write(response.content)
            print(f"{name} indirildi.")
        else:
            print(f"Hata: {url}")
    except Exception as e:
        print(f"Hata ({url}):", e)

# 📦 Zip dosyasına ekle
with ZipFile("All-Character-Traits.zip", 'w') as zipf:
    for name in file_names:
        path = f"chatgpt_gorselleri/{name}"
        if os.path.exists(path):
            zipf.write(path, arcname=name)

print("✅ Zip oluşturuldu: All-Character-Traits.zip")

driver.quit()
