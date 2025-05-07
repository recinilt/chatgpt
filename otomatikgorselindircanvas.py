import os
import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from zipfile import ZipFile

# 🗂️ Dosya isimleri
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

# 🚀 Tarayıcı başlat
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

# 💡 ChatGPT konuşma sayfasını aç (senin oturum açık olmalı!)
driver.get("https://chat.openai.com")

# Sayfanın yüklenmesini bekle
time.sleep(15)

# JavaScript ile canvas'lardaki görüntüleri base64 olarak çek
script = """
let canvases = document.querySelectorAll("canvas");
let results = [];
for (let canvas of canvases) {
    try {
        results.push(canvas.toDataURL("image/png"));
    } catch (e) {}
}
return results;
"""

# Base64 görselleri al
base64_images = driver.execute_script(script)

# 📂 Klasör oluştur
os.makedirs("chatgpt_canvas_gorselleri", exist_ok=True)

# 🎨 Görselleri kaydet
for idx, data_url in enumerate(base64_images):
    if idx >= len(file_names): break
    if data_url.startswith("data:image/png;base64,"):
        imgdata = base64.b64decode(data_url.split(",")[1])
        filepath = os.path.join("chatgpt_canvas_gorselleri", file_names[idx])
        with open(filepath, "wb") as f:
            f.write(imgdata)
        print(f"✅ Kaydedildi: {filepath}")

# 📦 Zip dosyası oluştur
with ZipFile("All-Character-Traits-CANVAS.zip", "w") as zipf:
    for name in file_names:
        fullpath = os.path.join("chatgpt_canvas_gorselleri", name)
        if os.path.exists(fullpath):
            zipf.write(fullpath, arcname=name)

print("📦 Tamamlandı: All-Character-Traits-CANVAS.zip")

driver.quit()
