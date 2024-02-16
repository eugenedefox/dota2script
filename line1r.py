import time
import ahk
import pyautogui
import asyncio

import keyboard


def active_window_1r():
    pyautogui.moveTo(540, 457)
    pyautogui.doubleClick()
    pyautogui.sleep(0.3)


active_window_1r()


def map_navigation_1r():
    ahk.mouse_move(555, 434, speed=60)
    pyautogui.sleep(1)
    ahk.right_click()


map_navigation_1r()

time.sleep(35)


def line_self_1r():
    pyautogui.sleep(3)
    pyautogui.press('f1')
    pyautogui.press('f1')
    pyautogui.sleep(1.2)
    pyautogui.press('f1')


line_self_1r()


def line_patrol_1r():
    pyautogui.sleep(4)
    pyautogui.press('p')
    ahk.mouse_move(388,225, speed=45.241)
    pyautogui.sleep(2)
    ahk.click()


line_patrol_1r()
