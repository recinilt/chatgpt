import time
import pyautogui
import webbrowser
import keyboard  # Türkçe karakter desteği için

# ChatGPT sayfasını aç
webbrowser.open("https://chatgpt.com/c/68176826-24b0-8003-bd95-da5f247773a7")
input("✍️ ChatGPT yüklensin ve hazır olunca ENTER'a bas: ")

# Yazma kutusunun koordinatları
yazi_kutusu_x = 1449
yazi_kutusu_y = 981

# Temel prompt
temel_prompt = "  "

# Çok satırlı prompt listesi
raw_prompts = '''
1. Create a Composition Close-up image with the character’s head clearly visible.
2. Create a Composition Extreme Close-up image with the character’s head clearly visible.
3. Create a Composition Medium Shot image with the character’s head clearly visible.
4. Create a Composition Wide Shot image with the character’s head clearly visible.
5. Create a Composition Extreme Wide Shot image with the character’s head clearly visible.
6. Create a Composition Top-down View image with the character’s head clearly visible.
7. Create a Composition Bird's Eye View image with the character’s head clearly visible.
8. Create a Composition Worm's Eye View image with the character’s head clearly visible.
9. Create a Composition Side View image with the character’s head clearly visible.
10. Create a Composition Front View image with the character’s head clearly visible.
11. Create a Composition Over the Shoulder image with the character’s head clearly visible.
12. Create a Composition Point of View (POV) image with the character’s head clearly visible.
13. Create a Composition Low Angle Shot image with the character’s head clearly visible.
14. Create a Composition High Angle Shot image with the character’s head clearly visible.
15. Create a Symmetrical Composition image with the character’s head clearly visible.
16. Create a Asymmetrical Composition image with the character’s head clearly visible.
17. Create a Rule of Thirds composition image with the character’s head clearly visible.
18. Create a Centered Composition image with the character’s head clearly visible.
19. Create a Diagonal Composition image with the character’s head clearly visible.
20. Create a Minimal Composition image with the character’s head clearly visible.
21. Create a Dynamic Composition image with the character’s head clearly visible.
22. Create a Crowded Composition image with the character’s head clearly visible.
23. Create a Negative Space Focused composition image with the character’s head clearly visible.
24. Create a Frame within a Frame composition image with the character’s head clearly visible.
25. Create a Leading Lines composition image with the character’s head clearly visible.
26. Create a Dutch Angle (Tilted Shot) composition image with the character’s head clearly visible.
27. Create a Silhouette Composition image with the character’s head clearly visible.
28. Create a Panoramic View composition image with the character’s head clearly visible.
29. Create a Overhead Composition image with the character’s head clearly visible.
30. Create a Inverted Composition image with the character’s head clearly visible.
31. Create a Contrast-heavy Composition image with the character’s head clearly visible.
32. Create a Layered Composition image with the character’s head clearly visible.
33. Create a Background-focused Composition image with the character’s head clearly visible.
34. Create a Foreground-focused Composition image with the character’s head clearly visible.
35. Create a Off-center Focused composition image with the character’s head clearly visible.
36. Create a Horizontal Composition image with the character’s head clearly visible.
37. Create a Vertical Composition image with the character’s head clearly visible.
38. Create a Depth-focused Composition image with the character’s head clearly visible.
39. Create a Tilted Frame composition image with the character’s head clearly visible.
40. Create a Zig-zag Eye Path composition image with the character’s head clearly visible.
41. Create a S-Curve Composition image with the character’s head clearly visible.
42. Create a L-Shape Layout composition image with the character’s head clearly visible.
43. Create a Golden Ratio Layout image with the character’s head clearly visible.
44. Create a Spiral Composition image with the character’s head clearly visible.
45. Create a Cylindrical Perspective composition image with the character’s head clearly visible.
46. Create a Spherical Perspective composition image with the character’s head clearly visible.
47. Create a Wide Angle Distortion composition image with the character’s head clearly visible.
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
    pyautogui.click(x=1260, y=969)
    time.sleep(1)
    pyautogui.click(x=1326, y=733)
    time.sleep(1)
    pyautogui.click(x=1052, y=691)
    time.sleep(1)
    pyautogui.click(x=1060, y=957)
    time.sleep(10)
    pyautogui.click(x=1167, y=721)
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
    time.sleep(20)

print("🎉 Tüm komutlar başarıyla gönderildi.")
