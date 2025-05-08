import time
import pyautogui
import webbrowser
import win32api
import win32con
import keyboard  # Türkçe karakter yazmak için

# ChatGPT sayfasını aç
webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
input("✍️ ChatGPT yüklensin ve hazır olunca ENTER'a bas: ")

# Yazma kutusunun koordinatları
yazi_kutusu_x = 1449
yazi_kutusu_y = 981

# Temel prompt
temel_prompt = " Hiperrealistik tarzda, karakterin ayak ve kafası dahil tüm bedeni uzaktan görünecek şekilde, uzak çekim, 1:1 ebatında, telif hakkı içermeyecek şekilde uyarla. "

# Çok satırlı prompt listesi
raw_prompts = '''
1. Character Traits: Human. görseli oluştur.
2. Character Traits: Child. görseli oluştur.
3. Character Traits: Teenager. görseli oluştur.
4. Character Traits: Adult. görseli oluştur.
5. Character Traits: Elderly. görseli oluştur.
'''

# Satırları listeye dönüştür
prompt_listesi = [satir.strip() for satir in raw_prompts.strip().split('\n') if satir.strip()]

# Ctrl + Enter tuş kombinasyonu fonksiyonu
def press_ctrl_enter():
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    time.sleep(0.05)
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
    time.sleep(0.05)
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

# Döngüyle sırayla gönder
for prompt in prompt_listesi:
    pyautogui.click(x=219, y=359)  # Prompt kutusuna tıkla
    time.sleep(0.3)
    tam_komut = prompt + temel_prompt
    keyboard.write(tam_komut, delay=0.05)  # Türkçe karakter desteğiyle yaz
    press_ctrl_enter()  # Gerçek Ctrl+Enter
    pyautogui.click(x=78, y=543)  # İstersen başka alana tıklayarak ekranı temizle
    print(f"✅ Gönderildi: {tam_komut}")
    time.sleep(10)

print("🎉 Tüm komutlar başarıyla gönderildi.")
