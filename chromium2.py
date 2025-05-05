import time
import pyautogui
import webbrowser

# ChatGPT sayfasını aç
webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
input("✍️ ChatGPT yüklensin ve hazır olunca ENTER'a bas: ")

# Yazma kutusunun X ve Y koordinatları (örnek)
yazi_kutusu_x = 1230
yazi_kutusu_y = 894

# Otomasyon döngüsü
while True:
    pyautogui.click(x=yazi_kutusu_x, y=yazi_kutusu_y)  # Yazı alanına tıkla
    time.sleep(0.3)
    pyautogui.write(" siradaki prompt ile gorseli olustur. ", interval=0.05)
    pyautogui.press("enter")
    print("✅ Komut gönderildi")
    time.sleep(150)
