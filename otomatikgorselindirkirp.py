import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
from zipfile import ZipFile

# 🔢 Dosya isimleri
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

# 🌐 Tarayıcı başlat
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# 📌 ChatGPT konuşma linkini buraya gir
driver.get("https://chat.openai.com/c/681baf35-9b70-8001-8b27-b25815929fcc")

time.sleep(10)  # Sayfa tam yüklensin

# 📂 Klasör hazırla
os.makedirs("kesilen_gorseller", exist_ok=True)

# ⬇️ <img> öğelerini topla (sadece OpenAI görselleri)
imgs = driver.find_elements(By.TAG_NAME, "img")
filtered_imgs = [img for img in imgs if img.get_attribute("src") and "sdmntprcentralus.oaiusercontent.com/files" in img.get_attribute("src")]

# 🔍 Her img öğesinin ekran görüntüsünü kes ve kaydet
for idx, (img, name) in enumerate(zip(filtered_imgs, file_names)):
    # Tam ekran görüntü al
    png = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(png))

    # Konum ve boyut bilgileri al
    location = img.location_once_scrolled_into_view
    size = img.size
    x, y = int(location['x']), int(location['y'])
    w, h = int(size['width']), int(size['height'])

    # Görseli kırp
    cropped = screenshot.crop((x, y, x + w, y + h))
    filepath = f"kesilen_gorseller/{name}"
    cropped.save(filepath)
    print(f"✅ Kesildi ve kaydedildi: {name}")

# 📦 ZIP oluştur
with ZipFile("All-Character-Traits-CROPPED.zip", 'w') as zipf:
    for name in file_names:
        fullpath = os.path.join("kesilen_gorseller", name)
        if os.path.exists(fullpath):
            zipf.write(fullpath, arcname=name)

print("🎉 ZIP hazır: All-Character-Traits-CROPPED.zip")
driver.quit()
