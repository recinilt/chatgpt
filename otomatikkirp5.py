import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
from zipfile import ZipFile

# 🔢 18 dosya ismi
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

# 🔧 Tarayıcıyı aç
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, use_subprocess=True)

# 📌 ChatGPT sayfasına git
driver.get("https://chat.openai.com/c/681baf35-9b70-8001-8b27-b25815929fcc")
input("🔐 Lütfen giriş yap ve Enter'a bas...")

# 🐌 Sayfayı aşağı kaydır ki lazy-load görseller yüklensin
scroll_pause_time = 1
for _ in range(30):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(scroll_pause_time)

# 📂 Klasör hazırla
os.makedirs("kesilen_gorseller", exist_ok=True)

# 🎯 Spesifik filtre: alt, class ve src bir arada
xpath = ("//img[@alt='Görsel üretildi' and "
         "contains(@class, 'absolute') and contains(@class, 'w-full') and "
         "contains(@src, 'sdmntprcentralus.oaiusercontent.com/files')]")

all_imgs = driver.find_elements(By.XPATH, xpath)

# ✅ İlk 18 tanesini sırayla işle
target_imgs = all_imgs[:18]
print(f"🔍 {len(target_imgs)} hedef görsel bulundu. İşleniyor...\n")

for idx, (img, name) in enumerate(zip(target_imgs, file_names)):
    try:
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", img)
        time.sleep(1)
        png = img.screenshot_as_png
        image = Image.open(BytesIO(png))
        image.save(f"kesilen_gorseller/{name}")
        print(f"✅ Kaydedildi: {name}")
    except Exception as e:
        print(f"❌ Hata [{name}]: {e}")

# 📦 ZIP oluştur
with ZipFile("All-Character-Traits-FINAL.zip", 'w') as zipf:
    for name in file_names:
        path = f"kesilen_gorseller/{name}"
        if os.path.exists(path):
            zipf.write(path, arcname=name)

print("🎉 ZIP hazır!")
driver.quit()
