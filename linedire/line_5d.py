import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_5d():
    pyautogui.moveTo(807,971)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_5d()
def map_navigation_5d():
    pydirectinput.moveTo(1253,10041)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_5d()



pyautogui.sleep(40)
