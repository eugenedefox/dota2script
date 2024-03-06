<<<<<<< HEAD
import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_3d():
    pyautogui.moveTo(1440,459)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_3d()
def map_navigation_3d():
    pydirectinput.moveTo(1844,469)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_3d()

pyautogui.sleep(40)


=======
import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_3d():
    pyautogui.moveTo(1440,459)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_3d()
def map_navigation_3d():
    pydirectinput.moveTo(1844,469)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_3d()

pyautogui.sleep(40)


>>>>>>> origin/main
