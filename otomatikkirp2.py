import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
from zipfile import ZipFile

# Dosya isimleri
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

# Tarayıcı başlat
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, use_subprocess=True)

# ChatGPT sayfasını aç
driver.get("https://chat.openai.com/c/681baf35-9b70-8001-8b27-b25815929fcc")
input("🔐 Lütfen giriş yap ve ardından Enter'a bas...")

# Klasör hazırla
os.makedirs("kesilen_gorseller", exist_ok=True)

# Görselleri bul
imgs = driver.find_elements(By.TAG_NAME, "img")
filtered_imgs = [img for img in imgs if img.get_attribute("src") and "sdmntprcentralus.oaiusercontent.com/files" in img.get_attribute("src")]

# Kes ve kaydet
for idx, (img, name) in enumerate(zip(filtered_imgs, file_names)):
    driver.execute_script("arguments[0].scrollIntoView(true);", img)
    time.sleep(1)
    screenshot = Image.open(BytesIO(driver.get_screenshot_as_png()))
    loc = img.location_once_scrolled_into_view
    size = img.size
    x, y = int(loc['x']), int(loc['y'])
    w, h = int(size['width']), int(size['height'])
    cropped = screenshot.crop((x, y, x + w, y + h))
    cropped.save(f"kesilen_gorseller/{name}")
    print(f"✅ {name} kaydedildi")

# ZIP oluştur
with ZipFile("All-Character-Traits-CROPPED.zip", 'w') as zipf:
    for name in file_names:
        path = f"kesilen_gorseller/{name}"
        if os.path.exists(path):
            zipf.write(path, arcname=name)

print("🎉 ZIP hazır!")
driver.quit()
