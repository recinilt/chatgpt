import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

# 🔧 Tarayıcı ayarları
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, use_subprocess=True)

# 📌 ChatGPT sayfası
driver.get("https://chat.openai.com/c/681baf35-9b70-8001-8b27-b25815929fcc")
input("🔐 Lütfen giriş yap ve ardından Enter'a bas...")

# 👇 Sayfanın en altına kadar kaydır (lazy-load çözümü)
scroll_pause_time = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 📂 Klasör hazırla
os.makedirs("kesilen_gorseller", exist_ok=True)

# 🎯 Görselleri bul
imgs = driver.find_elements(By.TAG_NAME, "img")
target_imgs = [img for img in imgs if img.get_attribute("src") and "sdmntprcentralus.oaiusercontent.com/files" in img.get_attribute("src")]

print(f"🔍 {len(target_imgs)} görsel bulundu.\n")

# 🔍 Her görseli tam olarak kes
for idx, (img, name) in enumerate(zip(target_imgs, file_names)):
    try:
        # Ortaya getir (daha isabetli ekran görüntüsü için)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", img)
        time.sleep(1)

        # Tam görsel ekran görüntüsü
        png = img.screenshot_as_png
        image = Image.open(BytesIO(png))
        image.save(f"kesilen_gorseller/{name}")
        print(f"✅ Kaydedildi: {name}")
    except Exception as e:
        print(f"❌ Hata [{name}]: {e}")

# 📦 ZIP oluştur
with ZipFile("All-Character-Traits-CROPPED-FULL.zip", 'w') as zipf:
    for name in file_names:
        path = f"kesilen_gorseller/{name}"
        if os.path.exists(path):
            zipf.write(path, arcname=name)

print("🎉 ZIP dosyası hazır!")
driver.quit()
