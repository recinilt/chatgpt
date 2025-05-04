import time
import pyautogui
import webbrowser

# 1. ChatGPT'deki özel linki aç
webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
print("🔗 ChatGPT sayfası açılıyor...")

# 2. Sayfanın tam yüklenmesi ve prompt'un yazılması için kullanıcıdan onay beklenir
input("✍️ Lütfen ChatGPT'de ilk prompt'u manuel olarak yaz ve ENTER'a basarak başlat: ")

# 3. Her 3 dakikada bir 'sıradaki görseli oluştur' yaz ve ENTER'a bas
while True:
    pyautogui.click()  # Aktif pencereye tıklayarak odağı al (önlem)
    time.sleep(0.5)    # Minik bekleme
    pyautogui.write("sıradaki görseli oluştur", interval=0.05)
    pyautogui.press("enter")
    print("✅ Komut gönderildi: sıradaki görseli oluştur")
    time.sleep(180)  # 3 dakika bekle
