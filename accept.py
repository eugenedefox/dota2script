import pyautogui
import keyboard
import sys
import time
from datetime import datetime, timedelta
# 3 урок сделай сам
# import win32api, win32con

from ahk import AHK

ahk = AHK()

import threading
from threading import Thread
from time import sleep

# path = 'BUTTONS/ready.png'

# for window in ahk.windows():
#    print(window.text)
#    print(window.id)
#    print(window.pid)
#    print(window.process_path)

stop = False


def EXIT():
    global stop

    while True:
        if keyboard.is_pressed("Esc"):
            stop = True
            pyautogui.sleep(0.05)
            break

        # В случае исключения в основном потоке, выходим и отправляем СТОП, чтобы закрылся этот поток.
        if stop == True:
            break
        pyautogui.sleep(0.05)

    # Запускаем поток (Запуск функции)
    th = Thread(target=EXIT)
    th.start()


# РАБОТАЕТ! Поиск окон по PID
# for window in ahk.windows():
#    print(window.text)
#    print(window.rect)
#    print(window.id)
#    print(window.pid)
#    print(window.process_path)

win = ahk.win_get(title='ahk_pid 10216')
if win:
    win.activate()

pyautogui.moveTo(565, 462, duration=0.75)
pyautogui.doubleClick()
pyautogui.sleep(0.2)
# program_list = pyautogui.getAllTitles()
# program_list

# for i in range (20):
#     if 'Диспетчер задач' in program_list:
#         break
#     sleep(1)


##########################################################################################

# while stop == False:

#     pyautogui.sleep(0.1)
#     ahk.key_press('q')
#     pyautogui.sleep(2)
#     ahk.key_press('w')
#     pyautogui.sleep(2)
#     Чтобы остановить цикл нужна многопоточность
# Для автозакупа скорее нужно будет выставлять большой sleep в районе 15 минут после фида

##########################################################################################

# ahk.mouse_move(x=100, y=100, speed=100, blocking=True)

##########################################################################################

timeStart = datetime.now()
timeFinish = timeStart + timedelta(seconds=720)

# 1 и 2 окно в разных группах
while timeStart < timeFinish:
    # image=r перед картинкой вставка
    button1 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720, confidence=0.9, region=(0, 0, 645, 510))
    button2 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720, confidence=0.9, region=(645, 0, 645, 510))
    pyautogui.doubleClick(button1)
    pyautogui.sleep(2)
    pyautogui.doubleClick(button2)
    button3 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720, confidence=0.9,
                                             region=(1449,202, 645, 510))
    pyautogui.doubleClick(button3)
    pyautogui.sleep(2.5)
    button4 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720, confidence=0.9,
                                             region=(0, 520, 645, 510))
    pyautogui.doubleClick(button4)
    pyautogui.sleep(2)
    button5 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720, confidence=0.9,
                                             region=(650, 520, 700, 700))
    pyautogui.doubleClick(button5)
    pyautogui.sleep(2)
        # прерывает цикл полностью
    timeStart = datetime.now()

    # button3 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720,confidence=0.9, region=(1275, 0, 645, 510))
    # button4 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720,confidence=0.9, region=(0, 520, 645, 510))
    # button5 = pyautogui.locateCenterOnScreen('accept.png', minSearchTime=720,confidence=0.9, region=(650, 520, 645, 510))

    pyautogui.sleep(0.3)