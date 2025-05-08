import time
import pyautogui
import webbrowser

# ChatGPT sayfasını aç
webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
input("✍️ ChatGPT yüklensin ve hazır olunca ENTER'a bas: ")

# Yazma kutusunun koordinatları
yazi_kutusu_x = 1449
yazi_kutusu_y = 981

# Temel prompt
temel_prompt = " Hiperrealistik tarzda. extreme wide shot. karakterin, ayak ve kafası dahil tüm bedeni uzaktan görünecek şekilde. 1:1 ebatında. telif hakkı içermeyecek şekilde uyarla. "

# Epostrof ile çok satırlı prompt listesi
raw_prompts = '''
37. Character Traits: Wizard. görseli oluştur.
38. Character Traits: Witch. görseli oluştur.
39. Character Traits: Mystic Monk. görseli oluştur.
40. Character Traits: Steampunk Adventurer. görseli oluştur.
41. Character Traits: Post-apocalyptic Survivor. görseli oluştur.
42. Character Traits: Time Traveler. görseli oluştur.
43. Character Traits: Cyberpunk Hacker. görseli oluştur.
44. Character Traits: Fantasy Hero. görseli oluştur.
45. Character Traits: Storybook Character. görseli oluştur.
46. Character Features: Animated Mascot. görseli oluştur.
47. Character Traits: Angel. görseli oluştur.
48. Character Traits: Ifrit (Ifrit / Fire Spirit). görseli oluştur.
49. Character Traits: Golem (Golem). görseli oluştur.
50. Character Traits: Puppet (Living Puppet). görseli oluştur.
51. Character Traits: Living Statue. görseli oluştur.
52. Character Traits: Cursed Prince (Cursed Prince). görseli oluştur.
53. Character Traits: Soul Carrier. görseli oluştur.
54. Character Traits: Sage. görseli oluştur.
'''

# Satır satır bölüp boşlukları temizleyerek listeye çevir
prompt_listesi = [satir.strip() for satir in raw_prompts.strip().split('\n') if satir.strip()]

# Döngüyle sırayla gönder
for prompt in prompt_listesi:
    pyautogui.click(x=yazi_kutusu_x, y=yazi_kutusu_y)
    time.sleep(0.3)
    tam_komut =  prompt + temel_prompt
    pyautogui.write(tam_komut, interval=0.05)
    #pyautogui.press("enter")
    pyautogui.click(x=1709, y=982)
    print(f"✅ Gönderildi: {tam_komut}")
    time.sleep(30)

print("🎉 Tüm komutlar başarıyla gönderildi.")
