import pyautogui
import time
time.sleep(4)
count=0
while count<=500:
    pyautogui.typewrite("I Love You "+str(count))
    pyautogui.press('enter')
    count = count+1