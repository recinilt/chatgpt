import time
import pyautogui
import webbrowser
import keyboard  # Türkçe karakter desteği için

# ChatGPT sayfasını aç
#webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
input("✍️ ChatGPT yüklensin ve hazır olunca ENTER'a bas: ")

# Yazma kutusunun koordinatları
yazi_kutusu_x = 1449
yazi_kutusu_y = 981

# Temel prompt
temel_prompt = "  "

# Çok satırlı prompt listesi
raw_prompts = '''
48. Create a Mirror Symmetry composition image with the character’s head clearly visible.
49. Create a Light-source Centered composition image with the character’s head clearly visible.
50. Create a Twisted Composition image with the character’s head clearly visible.
51. Create a Forced Perspective composition image with the character’s head clearly visible.
52. Create a Reflection-based Composition image with the character’s head clearly visible.
53. Create a Shadow-centered Composition image with the character’s head clearly visible.
54. Create a Stepped Arrangement composition image with the character’s head clearly visible.
55. Create a Chaotic Layout composition image with the character’s head clearly visible.
56. Create a Radiating from Center composition image with the character’s head clearly visible.
57. Create a Circular Composition image with the character’s head clearly visible.
58. Create a Exploding Layout composition image with the character’s head clearly visible.
59. Create a Intersecting Lines composition image with the character’s head clearly visible.
60. Create a Triangular Composition image with the character’s head clearly visible.
61. Create a Inverted Triangle Composition image with the character’s head clearly visible.
62. Create a Grid Composition image with the character’s head clearly visible.
63. Create a Chaotic Symmetry composition image with the character’s head clearly visible.
64. Create a Depth via Shading composition image with the character’s head clearly visible.
65. Create a Transition Between Layers (Layer Transition Focused) composition image with the character’s head clearly visible.
66. Create a Blended Background Composition image with the character’s head clearly visible.
67. Create a Isolated Subject Layout image with the character’s head clearly visible.
68. Create a Eye-guiding Flow composition image with the character’s head clearly visible.
69. Create a Three-layer Visual Hierarchy composition image with the character’s head clearly visible.
70. Create a Motion-directional Layout image with the character’s head clearly visible.
71. Create a Composition with Warped Perspective Layout image with the character’s head clearly visible.
72. Create a Staged Theatrical Composition image with the character’s head clearly visible.
'''

# Satırları listeye dönüştür
prompt_listesi = [satir.strip() for satir in raw_prompts.strip().split('\n') if satir.strip()]

# Döngüyle sırayla gönder
for prompt in prompt_listesi:
    pyautogui.click(x=680, y=946)
    time.sleep(1)
    pyautogui.click(x=727, y=885)
    time.sleep(1)
    pyautogui.click(x=1064, y=732)
    time.sleep(1)
    pyautogui.click(x=1080, y=955)
    time.sleep(10)
    pyautogui.click(x=1047, y=911)
    time.sleep(1)
    keyboard.send("ctrl+a")
    time.sleep(1)
    keyboard.send("del")
    time.sleep(1)
    tam_komut =  prompt + temel_prompt
    keyboard.write(tam_komut, delay=0.05)  # Türkçe karakter desteğiyle yaz
    #pyautogui.click(x=545, y=987)  # "Gönder" butonuna tıklama (ENTER yerine)
    keyboard.send("ctrl+enter")  # Gönderme: Ctrl + Enter
    time.sleep(3)
    #pyautogui.click(x=78, y=543)
    
    print(f"✅ Gönderildi: {tam_komut}")
    time.sleep(180)

print("🎉 Tüm komutlar başarıyla gönderildi.")
