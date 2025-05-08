import win32api
import win32con
import time

def press_ctrl_enter():
    # CTRL tuşuna bas
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    time.sleep(0.05)

    # ENTER tuşuna bas
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
    time.sleep(0.05)

    # ENTER tuşunu bırak
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.05)

    # CTRL tuşunu bırak
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

# Örnek kullanım
print("3 saniye sonra Ctrl + Enter gönderilecek...")
time.sleep(3)
press_ctrl_enter()
print("✅ Gönderildi!")
