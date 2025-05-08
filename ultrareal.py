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
temel_prompt = " with a minimalist black baby. hyperrealistic, square composition, 512x512 aspect ratio. fixed seed:8888 "

# Çok satırlı prompt listesi
raw_prompts = '''
1. Composition Close-up. görseli oluştur.
2. Composition Extreme Close-up. görseli oluştur.
3. Composition Medium Shot. görseli oluştur.
4. Composition Wide Shot. görseli oluştur.
5. Composition Extreme Wide Shot. görseli oluştur.
6. Composition Top-down View. görseli oluştur.
7. Composition Bird's Eye View. görseli oluştur.
8. Composition Worm's Eye View. görseli oluştur.
9. Composition Side View. görseli oluştur.
10. Composition Front View. görseli oluştur.
11. Composition Over the Shoulder. görseli oluştur.
12. Composition Point of View (POV). görseli oluştur.
13. Composition Low Angle Shot. görseli oluştur.
14. Composition High Angle Shot. görseli oluştur.
15. Composition Symmetrical Composition. görseli oluştur.
16. Composition Asymmetrical Composition. görseli oluştur.
17. Composition Rule of Thirds. görseli oluştur.
18. Composition Centered Composition. görseli oluştur.
19. Composition Diagonal Composition. görseli oluştur.
20. Composition Minimal Composition. görseli oluştur.
21. Composition Dynamic Composition. görseli oluştur.
22. Composition Crowded Composition. görseli oluştur.
23. Composition Negative Space Focused. görseli oluştur.
24. Composition Frame within a Frame. görseli oluştur.
25. Composition Leading Lines. görseli oluştur.
26. Composition Dutch Angle (Dutch Angle / Tilted Shot). görseli oluştur.
27. Composition Silhouette Composition. görseli oluştur.
28. Composition Panoramic View. görseli oluştur.
29. Composition Overhead Composition. görseli oluştur.
30. Composition Inverted Composition. görseli oluştur.
31. Composition Contrast-heavy Composition. görseli oluştur.
32. Composition Layered Composition. görseli oluştur.
33. Composition Background-focused Composition. görseli oluştur.
34. Composition Foreground-focused Composition. görseli oluştur.
35. Composition Off-center Focused. görseli oluştur.
36. Composition Horizontal Composition. görseli oluştur.
37. Composition Vertical Composition. görseli oluştur.
38. Composition Depth-focused Composition. görseli oluştur.
39. Composition Tilted Frame. görseli oluştur.
40. Composition Zig-zag Eye Path. görseli oluştur.
41. Composition S-Curve Composition. görseli oluştur.
42. Composition L-Shape Layout. görseli oluştur.
43. Composition Golden Ratio Layout. görseli oluştur.
44. Composition Spiral Composition. görseli oluştur.
45. Composition Cylindrical Perspective. görseli oluştur.
46. Composition Spherical Perspective. görseli oluştur.
47. Composition Wide Angle Distortion. görseli oluştur.
48. Composition Mirror Symmetry. görseli oluştur.
49. Composition Light-source Centered. görseli oluştur.
50. Composition Twisted Composition. görseli oluştur.
51. Composition Forced Perspective. görseli oluştur.
52. Composition Reflection-based Composition. görseli oluştur.
53. Composition Shadow-centered Composition. görseli oluştur.
54. Composition Stepped Arrangement. görseli oluştur.
55. Composition Chaotic Layout. görseli oluştur.
56. Composition Radiating from Center. görseli oluştur.
57. Composition Circular Composition. görseli oluştur.
58. Composition Exploding Layout. görseli oluştur.
59. Composition Intersecting Lines. görseli oluştur.
60. Composition Triangular Composition. görseli oluştur.
61. Composition Inverted Triangle Composition. görseli oluştur.
62. Composition Grid Composition. görseli oluştur.
63. Composition Chaotic Symmetry. görseli oluştur.
64. Composition Depth via Shading. görseli oluştur.
65. Composition Transition Between Layers (Layer Transition Focused). görseli oluştur.
66. Composition Blended Background Composition. görseli oluştur.
67. Composition Isolated Subject Layout. görseli oluştur.
68. Composition Eye-guiding Flow. görseli oluştur.
69. Composition Three-layer Visual Hierarchy. görseli oluştur.
70. Composition Motion-directional Layout. görseli oluştur.
71. Composition Composition with Warped Perspective Layout. görseli oluştur.
72. Composition Staged Theatrical Composition. görseli oluştur.
'''

# Satırları listeye dönüştür
prompt_listesi = [satir.strip() for satir in raw_prompts.strip().split('\n') if satir.strip()]

# Döngüyle sırayla gönder
for prompt in prompt_listesi:
    pyautogui.click(x=471, y=468)
    time.sleep(1)
    keyboard.send("ctrl+a")
    time.sleep(1)
    keyboard.send("del")
    time.sleep(1)
    tam_komut =  prompt + temel_prompt
    keyboard.write(tam_komut, delay=0.05)  # Türkçe karakter desteğiyle yaz
    #pyautogui.click(x=545, y=987)  # "Gönder" butonuna tıklama (ENTER yerine)
    #keyboard.send("ctrl+enter")  # Gönderme: Ctrl + Enter
    pyautogui.click(x=481, y=731)
    time.sleep(3)
    #pyautogui.click(x=78, y=543)
    
    print(f"✅ Gönderildi: {tam_komut}")
    time.sleep(25)

print("🎉 Tüm komutlar başarıyla gönderildi.")
