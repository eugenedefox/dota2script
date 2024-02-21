import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_4d():
    pyautogui.moveTo(163,977)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_4d()
def map_navigation_4d():
    pydirectinput.moveTo(573,976)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_4d()

pyautogui.sleep(40)


