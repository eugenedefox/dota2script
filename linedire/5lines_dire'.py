import time
from ahk import AHK
ahk = AHK()
import pyautogui
import asyncio

import pydirectinput
import keyboard

def active_window_1d():
    pyautogui.moveTo(164,460)
    pydirectinput.doubleClick()
    time.sleep(0.3)


active_window_1d()
def map_navigation_1d():
    pydirectinput.moveTo(546,423)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_1d()



pyautogui.sleep(40)
def map_navigation_1d_2move():
    pyautogui.sleep(0.3)
    pydirectinput.moveTo(542,446)
    pyautogui.sleep(0.3)
    ahk.right_click()

map_navigation_1d_2move()


time.sleep(3)

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

map_navigation_2d_2move()


time.sleep(3)


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

pyautogui.sleep(3)

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

pyautogui.sleep(3)

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