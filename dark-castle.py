from pyautogui import click as Click
from pyautogui import moveTo as MouseMove
from pyautogui import press as Send
from time import sleep as Sleep

Click(800, 900)         # Play
Sleep(0.001*500)
Click(1400, 950)        # Expert
Sleep(0.001*500)
Click(1645, 435)
Sleep(0.001*500)
Click(945, 210)         # Dark Castle
Sleep(0.001*500)
Click(550, 400)         # Easy
Sleep(0.001*500)
Click(550, 600)         # Standard
Sleep(0.001*5000)
while True:
    Send("space")       # Start game
    Sleep(0.001*100)
    Send("space")       # Increase Speed
    Send("u")           # Hero (Obyn)
    Sleep(0.001*100)
    Click(549, 617)
    Sleep(0.001*100)
    Send("q")           # Dart
    MouseMove(549, 500)
    Sleep(0.001*2000)
    Click(549, 489)
    Sleep(0.001*100)
    Click(549, 489)
    Sleep(0.001*200)
    Send("/")           # Dart -> 0-0-1
    Sleep(0.001*100)
    Click(785, 555)
    Sleep(0.001*100)
    #
    MouseMove(1500, 1000)
    for i in range(9):
        Sleep(0.001*1380)
        Click()
    #
    MouseMove(1084, 409)
    Sleep(0.001*100)
    Send("x")            # Monkey Sub
    Sleep(0.001*100)
    Click(1084, 409)
    Sleep(0.001*100)
    Click(1084, 409)
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(10):
        Sleep(0.001*2680)
        Click()
    #
    Click(1084, 409)
    Sleep(0.001*100)
    Send(",")            # Sub -> 1-0-0
    Sleep(0.001*100)
    Send(",")            # Sub -> 2-0-0
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(10):
        Sleep(0.001*2180)
        Click()
    #
    Click(1084, 409)
    Sleep(0.001*100)
    Send("/")            # Sub -> 2-0-1
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(9):
        Sleep(0.001*4880)
        Click()
    #
    Click(1084, 409)
    Sleep(0.001*100)
    Send("/")            # Sub -> 2-0-2
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(9):
        Sleep(0.001*4080)
        Click()
    #
    Click(1084, 409)
    Sleep(0.001*100)
    Send("/")            # Sub -> 2-0-3
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(10):
        Sleep(0.001*5980)
        Click()
    #
    Click(1084, 409)
    Sleep(0.001*100)
    Send("/")            # Sub -> 2-0-4
    Click(549, 489)
    Sleep(0.001*200)
    Send("/")            # Dart -> 0-0-2
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(10):
        Sleep(0.001*5850)
        Click()
    #
    MouseMove(960, 430)
    Sleep(0.001*100)
    Send("k")            # Monkey Village
    Click(960, 430)
    Sleep(0.001*100)
    Click(960, 430)
    Sleep(0.001*200)
    Send(".")
    Sleep(0.001*100)
    Send(".")
    Sleep(0.001*100)
    Send(",")
    Sleep(0.001*100)
    Send(",")
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(9):
        Sleep(0.001*3700)
        Click()
    #
    MouseMove(770, 430)
    Sleep(0.001*100)
    Send("a")           # Monkey Wizard
    Sleep(0.001*100)
    Click(770, 430)
    Sleep(0.001*100)
    Click(770, 430)
    Send(".")
    Sleep(0.001*200)
    Send(".")
    Sleep(0.001*100)
    Send(".")
    Sleep(0.001*100)
    #
    Click(1500, 1000)
    for i in range(9):
        Sleep(0.001*1000)
        Click()
    #
    MouseMove(960, 920)
    Sleep(0.001*100)
    Click()
    Sleep(0.001*1300)
    Click(1265, 835)
    Sleep(0.001*1400)
    MouseMove(1140, 730)
    Click()
    Sleep(0.001*1300)
    Click(1050, 911)     # Freeplay
    Sleep(0.001*1000)
    Click(980, 770)     # Ok
    Sleep(0.001*1500)
    Click(1600, 40)     # Menu
    Sleep(0.001*1000)
    Click(1070, 850)    # Restart
    Sleep(0.001*1000)
    Click(1140, 730)    # Confirm
    Sleep(0.001*1500)
    MouseMove(549, 617)
    Sleep(0.001*500)