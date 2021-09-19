import pyautogui
import time
time.sleep(5)
f = open('wildest.txt', 'r')

for word in f:
    print(word)
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(5)
