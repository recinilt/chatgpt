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
temel_prompt = " 1:1 ebatında. "

# Çok satırlı prompt listesi
raw_prompts = '''
1. Emotion Happy. görseli oluştur.
2. Emotion Sad (Sad). görseli oluştur.
3. Emotion Angry. görseli oluştur.
4. Emotion Fearful. görseli oluştur.
5. Emotion Surprised. görseli oluştur.
6. Emotion Disgusted. görseli oluştur.
7. Emotion Confused. görseli oluştur.
8. Emotion Excited. görseli oluştur.
9. Emotion Lonely. görseli oluştur.
10. Emotion Hopeful. görseli oluştur.
11. Emotion Depressed. görseli oluştur.
12. Emotion Melancholic. görseli oluştur.
13. Emotion Romantic. görseli oluştur.
14. Emotion Peaceful. görseli oluştur.
15. Emotion Calm. görseli oluştur.
16. Emotion Joyful. görseli oluştur.
17. Emotion Satisfied (Content). görseli oluştur.
18. Emotion Energetic. görseli oluştur.
19. Emotion Playful. görseli oluştur.
20. Emotion Anxious. görseli oluştur.
21. Emotion Terrified. görseli oluştur.
22. Emotion Grieving. görseli oluştur.
23. Emotion Optimistic. görseli oluştur.
24. Emotion Pessimistic. görseli oluştur.
25. Emotion Nostalgic. görseli oluştur.
26. Emotion Frustrated. görseli oluştur.
27. Emotion Amazed. görseli oluştur.
28. Emotion Proud. görseli oluştur.
29. Emotion Ashamed (Ashamed). görseli oluştur.
30. Emotion Bored. görseli oluştur.
31. Emotion Curious. görseli oluştur.
32. Emotion Courageous. görseli oluştur.
33. Emotion Jealous. görseli oluştur.
34. Emotion Embarrassed. görseli oluştur.
35. Emotion Grateful. görseli oluştur.
36. Emotion Feeling Guilty. görseli oluştur.
37. Emotion Serene. görseli oluştur.
38. Emotion Silly. görseli oluştur.
39. Emotion Determined. görseli oluştur.
40. Emotion Relaxed. görseli oluştur.
41. Emotion Panicked. görseli oluştur.
42. Emotion Inner Peace. görseli oluştur.
43. Emotion Distracted. görseli oluştur.
44. Emotion Uneasy. görseli oluştur.
45. Emotion Disappointed. görseli oluştur.
46. Emotion Inspired. görseli oluştur.
47. Emotion Silent Rage. görseli oluştur.
48. Emotion Ecstatic. görseli oluştur.
49. Emotion Touched. görseli oluştur.
50. Emotion Cool-headed. görseli oluştur.
51. Emotion Confident. görseli oluştur.
52. Emotion Introverted. görseli oluştur.
53. Emotion Extroverted. görseli oluştur.
54. Emotion Alert and Vigilant (Alert). görseli oluştur.
55. Emotion Drowsy. görseli oluştur.
56. Feeling Numb. görseli oluştur.
57. Emotion Mixture of Fear and Curiosity (Fearful Curiosity). görseli oluştur.
58. Emotion Daydreaming. görseli oluştur.
59. Emotion Hopeless. görseli oluştur.
60. Emotion Affectionate. görseli oluştur.
61. Emotion Compassionate. görseli oluştur.
62. Emotion Hateful. görseli oluştur.
63. Emotion Soulful Sorrow. görseli oluştur.
64. Emotion Crying with Joy. görseli oluştur.
65. Emotion Overthinking. görseli oluştur.
66. Emotion Present-focused. görseli oluştur.
67. Emotion Lost in Thought. görseli oluştur.
68. Emotion: Vengeful. görseli oluştur.
69. Emotion Suspicious. görseli oluştur.
70. Emotion Carefree. görseli oluştur.
71. Emotion In the Flow. görseli oluştur.
72. Emotion Enlightened. görseli oluştur.
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
    pyautogui.click(x=683, y=911)
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
