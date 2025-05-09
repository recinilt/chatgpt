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
temel_prompt = " realistic."

# Çok satırlı prompt listesi
raw_prompts = '''
1. Location: Forest.  .
2. Venue: Dense Jungle.  .
3. Location: Desert.  .
4. Venue: Beach.  .
5. Venue: Ocean Underwater.  .
6. Place: Mountains.  .
7. Venue: Canyon.  .
8. Venue: Savana (Savannah).  .
9. Venue: Frozen Tundra.  .
10. Venue: Glacier.  .
11. Venue: City.  .
12. Venue: Futuristic City.  .
13. Venue: Abandoned City.  .
14. Venue: Small Village.  .
15. Venue: Castle.  .
16. Venue: Medieval Town.  .
17. Venue: Ancient Ruins.  .
18. Venue: Temple.  .
19. Venue: Cave.  .
20. Venue: Volcano.  .
21. Venue: Space Station.  .
22. Venue: Alien Planet.  .
23. Venue: Floating Island.  .
24. Venue: Sky Kingdom.  .
25. Venue: Underwater City.  .
26. Venue: Fantasy Land.  .
27. Venue: Sci-fi World.  .
28. Venue: Haunted Forest.  .
29. Venue: Dreamscape.  .
30. Venue: Cyberpunk Alley.  .
31. Venue: Steampunk Town.  .
32. Location: Post-apocalyptic Wasteland.  .
33. Venue: Snowy Village.  .
34. Venue: Sunny Meadow.  .
35. Venue: Flower Field.  .
36. Venue: Riverbank.  .
37. Venue: Misty Swamp.  .
38. Venue: Sunken Shipwreck.  .
39. Venue: City Rooftop.  .
40. Venue: Abandoned Amusement Park.  .
41. Venue: Spaceship Cockpit.  .
42. Venue: Ice Cave.  .
43. Venue: Ancient Arena.  .
44. Venue: Royal Palace.  .
45. Location: Dungeon.  .
46. Venue: Secret Garden.  .
47. Venue: Modern Art Gallery.  .
48. Venue: Airport (Airport Terminal).  .
49. Venue: Train Station.  .
50. Venue: Wizard Academy.  .
51. Venue: Time Travel Lab.  .
52. Venue: Lost Civilization's Center.  .
53. Venue: Wild West Town.  .
54. Venue: Gothic Cathedral.  .
55. Venue: Subconscious Realm.  .
56. Venue: Massive Library.  .
57. Venue: Hotel of Dreams (Dream Hotel).  .
58. Venue: Giant Clockwork Interior.  .
59. Venue: Inside a Flying Train.  .
60. Venue: Floating City on Water.  .
61. Venue: Inverted World.  .
62. Venue: Valley of Giant Plants.  .
63. Venue: Ghost Town.  .
64. Venue: Sci-fi Subway System.  .
65. Venue: Plasma Temple.  .
66. Venue: Mirror Maze.  .
67. Venue: Color-changing Forest.  .
68. Venue: Underground Kingdom.  .
69. Venue: Skywalk Between Skyscrapers.  .
70. Venue: Frozen Schoolyard.  .
71. Venue: Lost Island.  .
72. Venue: Colossal Shadow Crater.  .
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
    time.sleep(30)

print("🎉 Tüm komutlar başarıyla gönderildi.")
