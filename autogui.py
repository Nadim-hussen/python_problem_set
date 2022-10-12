import pyautogui
import time
time.sleep(4)
count=0
while count<=350:
    pyautogui.typewrite("hello bondhu sob bala nis"+str(count))
    pyautogui.press('enter')
    count = count+1