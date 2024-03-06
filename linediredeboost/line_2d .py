<<<<<<< HEAD
import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_2d():
    pyautogui.moveTo(804,467)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_2d()
def map_navigation_2d():
    pydirectinput.moveTo(1183,421)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_2d()



pyautogui.sleep(40)
def map_navigation_2d_2move():
    pyautogui.sleep(0.3)
    pydirectinput.moveTo(1179,448)
    pyautogui.sleep(0.3)
    ahk.right_click()

=======
import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_2d():
    pyautogui.moveTo(804,467)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_2d()
def map_navigation_2d():
    pydirectinput.moveTo(1183,421)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_2d()



pyautogui.sleep(40)
def map_navigation_2d_2move():
    pyautogui.sleep(0.3)
    pydirectinput.moveTo(1179,448)
    pyautogui.sleep(0.3)
    ahk.right_click()

>>>>>>> origin/main
map_navigation_2d_2move()