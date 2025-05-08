import time
import pyautogui
import webbrowser
import win32api
import win32con

# ChatGPT sayfasını aç
webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
input("✍️ ChatGPT yüklensin ve hazır olunca ENTER'a bas: ")

# Yazma kutusunun koordinatları
yazi_kutusu_x = 1449
yazi_kutusu_y = 981

# Temel prompt (sadece ASCII karakterler kullanılmalı!)
temel_prompt = " Hiperrealistic style, full-body visible, wide shot, 1:1 ratio, copyright-free adaptation. "

# Çok satırlı prompt listesi (sadece ASCII karakterli olmalı)
raw_prompts = '''
1. Character Traits: Human. generate image.
2. Character Traits: Child. generate image.
3. Character Traits: Teenager. generate image.
4. Character Traits: Adult. generate image.
5. Character Traits: Elderly. generate image.
'''

# Satırları listeye dönüştür
prompt_listesi = [satir.strip() for satir in raw_prompts.strip().split('\n') if satir.strip()]

# Ctrl + Enter tuş kombinasyonu
def press_ctrl_enter():
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    time.sleep(0.05)
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
    time.sleep(0.05)
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

# win32api ile karakter karakter yazma (sadece İngilizce karakterlerle çalışır)
def type_text(text):
    for char in text:
        vk = win32api.VkKeyScan(char)
        if vk == -1:
            print(f"⚠️ Yazılamadı: {char}")
            continue
        key = vk & 0xff
        shift_state = (vk >> 8) & 0xff

        if shift_state:
            win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
        win32api.keybd_event(key, 0, 0, 0)
        time.sleep(0.01)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
        if shift_state:
            win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.01)

# Gönderme döngüsü
for prompt in prompt_listesi:
    pyautogui.click(x=219, y=359)  # Yazma alanına tıkla
    time.sleep(0.3)
    tam_komut = prompt + temel_prompt
    print(f"⌨️ Yazılıyor: {tam_komut}")
    type_text(tam_komut)
    press_ctrl_enter()
    time.sleep(3)
    pyautogui.click(x=78, y=543)  # Odak başka yere al (isteğe bağlı)
    print(f"✅ Gönderildi.")
    time.sleep(10)

print("🎉 Tüm komutlar başarıyla gönderildi.")
