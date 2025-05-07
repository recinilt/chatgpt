import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
from zipfile import ZipFile

# 🔢 Dosya isimleri (sırasıyla)
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

# 📂 Kayıt klasörü
output_folder = "kesilen_gorseller"
os.makedirs(output_folder, exist_ok=True)

# 🧠 Profil dizini (senin Chrome profilin)
user_data_dir = r"C:\Users\RecepYeni\AppData\Local\Google\Chrome\User Data"

# 🌐 Tarayıcı başlat (senin profilinle)
options = Options()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument("--profile-directory=Default")  # Gerekirse 'Profile 1' yap
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# 🔗 ChatGPT konuşma sayfan
driver.get("https://chat.openai.com/c/681baf35-9b70-8001-8b27-b25815929fcc")

# Sayfanın yüklenmesini bekle
time.sleep(15)

# 🔍 OpenAI'nin oluşturduğu <img> görsellerini bul
imgs = driver.find_elements(By.TAG_NAME, "img")
filtered_imgs = [img for img in imgs if img.get_attribute("src") and "sdmntprcentralus.oaiusercontent.com/files" in img.get_attribute("src")]

# 🔪 Her görselin ekran görüntüsünü kes
for idx, (img, name) in enumerate(zip(filtered_imgs, file_names)):
    # Görselin görünmesini sağla
    driver.execute_script("arguments[0].scrollIntoView(true);", img)
    time.sleep(1)

    # Tam ekran görüntüsü al
    png = driver.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(png))

    # Konum ve boyut bilgisi al
    location = img.location_once_scrolled_into_view
    size = img.size
    x, y = int(location['x']), int(location['y'])
    w, h = int(size['width']), int(size['height'])

    # Kırp ve kaydet
    cropped = screenshot.crop((x, y, x + w, y + h))
    save_path = os.path.join(output_folder, name)
    cropped.save(save_path)
    print(f"✅ Kaydedildi: {name}")

# 📦 ZIP oluştur
zip_path = "All-Character-Traits-CROPPED.zip"
with ZipFile(zip_path, 'w') as zipf:
    for name in file_names:
        fullpath = os.path.join(output_folder, name)
        if os.path.exists(fullpath):
            zipf.write(fullpath, arcname=name)

print(f"\n🎉 ZIP hazır: {zip_path}")
driver.quit()
