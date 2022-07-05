import pyautogui
wh = pyautogui.size()
print(wh.width)


#moving the mouse and drawing a square 10 times.
for i in range(10):
    pyautogui.move(100, 0, duration=0.25)
    pyautogui.move(0, 100, duration=0.25)
    pyautogui.move(-100, 0, duration=0.25)
    pyautogui.move(0, -100, duration=0.25)
    

    