# Use Geraldo as hero
# Play on Cubism (Easy, Standard)
# Turn off Autostart

import pyautogui
import time

buffer = 0.2
Next = (960, 920)
Freeplay = (1250, 850)
OK = (950, 750)
Pause = (1600, 50)
Restart = (1050,850)
Confirm = (1150,725)
Shop = (1200,200)
esc = (300,800)
u1 = (667,514)
nft1 = (1300,350)
nft2 = (824,11)
q1 = (489,427)
h1 = (107,1011)
r1 = (621,590)
h2 = (269,1011)
h3 = (107,870)
k1 = (248,888)
f1 = (513,654)
h4 = (431,1011)
h5 = (107,729)
h6 = (389,870)
k2 = (531,556)

def Rounds():
    # Round 1
    for i in range(2):
        pyautogui.press("space")
        time.sleep(buffer)
    print("Round 1")
    pyautogui.press("u")
    time.sleep(buffer)
    pyautogui.moveTo(u1)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.press("q")
    time.sleep(buffer)
    pyautogui.moveTo(q1)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep((17.51+0)/3)
    # Round 2
    pyautogui.press("space")
    print("Round 2")
    time.sleep((19.00+3)/3)
    # Round 3
    pyautogui.press("space")
    print("Round 3")
    time.sleep((16.71+3)/3)
    # Round 4
    pyautogui.press("space")
    print("Round 4")
    time.sleep((17.31+3)/3)
    # Round 5
    pyautogui.press("space")
    print("Round 5")
    time.sleep((16.50+4)/3)
    # Round 6
    pyautogui.press("space")
    print("Round 6")
    pyautogui.press("u")
    time.sleep(buffer)
    pyautogui.click(Shop)
    time.sleep(buffer)
    pyautogui.click(nft1)
    time.sleep(buffer)
    pyautogui.moveTo(nft2)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(Shop)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((18.70+0)/3)
    # Round 7
    pyautogui.press("space")
    print("Round 7")
    time.sleep((26.80+4)/3)
    # Round 8
    pyautogui.press("space")
    print("Round 8")
    time.sleep((28.87+10)/3)
    # Round 9
    pyautogui.press("space")
    print("Round 9")
    time.sleep((18.95+11)/3)
    # Round 10
    pyautogui.press("space")
    print("Round 10")
    time.sleep((47.99+10)/3)
    # Round 11
    pyautogui.press("space")
    print("Round 11")
    pyautogui.press("h")
    time.sleep(buffer)
    pyautogui.moveTo(h1)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep((19.16+5)/3)
    # Round 12
    pyautogui.press("space")
    print("Round 12")
    time.sleep((17.39+10)/3)
    # Round 13
    pyautogui.press("space")
    print("Round 13")
    pyautogui.click(h1)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((32.21+9)/3)
    # Round 14
    pyautogui.press("space")
    print("Round 14")
    pyautogui.click(h1)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((26.63+10)/3)
    # Round 15
    pyautogui.press("space")
    print("Round 15")
    pyautogui.press("r")
    time.sleep(buffer)
    pyautogui.moveTo(r1)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((25.00+8)/3)
    # Round 16
    pyautogui.press("space")
    print("Round 16")
    pyautogui.click(r1)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((16.02+5)/3)
    # Round 17
    pyautogui.press("space")
    print("Round 17")
    time.sleep((5.00+10)/3)
    # Round 18
    pyautogui.press("space")
    print("Round 18")
    time.sleep((26.82+10)/3)
    # Round 19
    pyautogui.press("space")
    print("Round 19")
    pyautogui.press("h")
    time.sleep(buffer)
    pyautogui.moveTo(h2)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep((15.76+5)/3)
    # Round 20
    pyautogui.press("space")
    print("Round 20")
    pyautogui.click(h2)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((5.25+10)/3)
    # Round 21
    pyautogui.press("space")
    print("Round 21")
    pyautogui.click(h2)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(r1)
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((18.12+5)/3)
    # Round 22
    pyautogui.press("space")
    print("Round 22")
    time.sleep((8.00+10)/3)
    # Round 23
    pyautogui.press("space")
    print("Round 23")
    pyautogui.press("h")
    time.sleep(buffer)
    pyautogui.moveTo(h3)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep((6.82+10)/3)
    # Round 24
    pyautogui.press("space")
    print("Round 24")
    pyautogui.click(h3)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((9.00+20)/3)
    # Round 25
    pyautogui.press("space")
    print("Round 25")
    time.sleep((21.14+10)/3)
    # Round 26
    pyautogui.press("space")
    print("Round 26")
    pyautogui.press("k")
    time.sleep(buffer)
    pyautogui.moveTo(k1)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(k1)
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((14.51+8)/3)
    # Round 27
    pyautogui.press("space")
    print("Round 27")
    pyautogui.click(k1)
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((34.26+8)/3)
    # Round 28
    pyautogui.press("space")
    print("Round 28")
    pyautogui.click(h1)
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press("f")
    time.sleep(buffer)
    pyautogui.moveTo(f1)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((5.00+13)/3)
    # Round 29
    pyautogui.press("space")
    print("Round 29")
    pyautogui.click(h2)
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((15.25+5)/3)
    # Round 30
    pyautogui.press("space")
    print("Round 30")
    pyautogui.click(h3)
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(f1)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((13.07+8)/3)
    # Round 31
    pyautogui.press("space")
    print("Round 31")
    pyautogui.click(f1)
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((15.91+5)/3)
    # Round 32
    pyautogui.press("space")
    print("Round 32")
    pyautogui.press("h")
    time.sleep(buffer)
    pyautogui.moveTo(h4)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(h4)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((27.96+5)/3)
    # Round 33
    pyautogui.press("space")
    print("Round 33")
    pyautogui.click(h4)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(q1)
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((25.34+5)/3)
    # Round 34
    pyautogui.press("space")
    print("Round 34")
    pyautogui.click(h4)
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((36.00+5)/3)
    # Round 35
    pyautogui.press("space")
    print("Round 35")
    pyautogui.press("h")
    time.sleep(buffer)
    pyautogui.moveTo(h5)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(h5)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((33.76+5)/3)
    # Round 36
    pyautogui.press("space")
    print("Round 36")
    pyautogui.click(k1)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(h5)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((20.99+5)/3)
    # Round 37
    pyautogui.press("space")
    print("Round 37")
    pyautogui.click(h1)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((43.51+10)/3)
    # Round 38
    pyautogui.press("space")
    print("Round 38")
    pyautogui.click(h2)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((29.06+12)/3)
    # Round 39
    pyautogui.press("space")
    print("Round 39")
    pyautogui.click(h3)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((37.93+15)/3)
    # Round 40
    pyautogui.press("space")
    print("Round 40")
    pyautogui.press("h")
    time.sleep(buffer)
    pyautogui.moveTo(h6)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(h6)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((1.00+20)/3)
    # Round 41
    pyautogui.click(Next)
    time.sleep(1)
    pyautogui.click(Freeplay)
    time.sleep(1)
    pyautogui.click(OK)
    time.sleep(1)
    pyautogui.press("space")
    print("Round 41")
    pyautogui.click(r1)
    time.sleep(buffer)
    pyautogui.press("/")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((46.20+10)/3)
    # Round 42
    pyautogui.press("space")
    print("Round 42")
    pyautogui.press("k")
    time.sleep(buffer)
    pyautogui.moveTo(k2)
    time.sleep(buffer)
    pyautogui.click()
    time.sleep(buffer)
    pyautogui.click(k2)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.press(".")
    time.sleep(buffer)
    pyautogui.click(h4)
    time.sleep(buffer)
    pyautogui.press(",")
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep(buffer)
    pyautogui.click(esc)
    time.sleep((11.60+10)/3)
    # Round 43
    pyautogui.press("space")
    print("Round 43")
    time.sleep((9.26+10)/3)
    # Round 44
    pyautogui.press("space")
    print("Round 44")
    time.sleep((23.67+10)/3)
    # Round 45
    pyautogui.press("space")
    print("Round 45")
    time.sleep((53.10+10)/3)
    # Round 46
    pyautogui.press("space")
    print("Round 46")
    time.sleep((7.00+10)/3)
    # Round 47
    pyautogui.press("space")
    print("Round 47")
    time.sleep((24.65+10)/3)
    # Round 48
    pyautogui.press("space")
    print("Round 48")
    time.sleep((55.72+10)/3)
    # Round 49
    pyautogui.press("space")
    print("Round 49")
    time.sleep((50.00+10)/3)
    # Round 50
    pyautogui.press("space")
    print("Round 50")
    time.sleep((28.98+10)/3)
    # Round 51
    pyautogui.press("space")
    print("Round 51")
    time.sleep((24.14+10)/3)
    # Round 52
    pyautogui.press("space")
    print("Round 52")
    time.sleep((20.56+10)/3)
    # Round 53
    pyautogui.press("space")
    print("Round 53")
    time.sleep((35.00+10)/3)
    # Round 54
    pyautogui.press("space")
    print("Round 54")
    time.sleep((19.41+10)/3)
    # Round 55
    pyautogui.press("space")
    print("Round 55")
    time.sleep((29.78+10)/3)
    # Round 56
    pyautogui.press("space")
    print("Round 56")
    time.sleep((16.18+10)/3)
    # Round 57
    pyautogui.press("space")
    print("Round 57")
    time.sleep((26.23+10)/3)
    # Round 58
    pyautogui.press("space")
    print("Round 58")
    time.sleep((43.98+10)/3)
    # Round 59
    pyautogui.press("space")
    print("Round 59")
    time.sleep((26.16+10)/3)
    # Round 60
    pyautogui.press("space")
    print("Round 60")
    time.sleep((1.00+10)/3)
    # Round 61
    pyautogui.press("space")
    print("Round 61")
    time.sleep((20.00+10)/3)
    # Round 62
    pyautogui.press("space")
    print("Round 62")
    time.sleep((48.29+10)/3)
    # Round 63
    pyautogui.press("space")
    print("Round 63")
    time.sleep((42.25+10)/3)
    # Round 64
    pyautogui.press("space")
    print("Round 64")
    time.sleep((9.53+10)/3)
    # Round 65
    pyautogui.press("space")
    print("Round 65")
    time.sleep((62.00+10)/3)
    # Round 66
    pyautogui.press("space")
    print("Round 66")
    time.sleep((22.75+10)/3)
    # Round 67
    pyautogui.press("space")
    print("Round 67")
    time.sleep((26.44+10)/3)
    # Round 68
    pyautogui.press("space")
    print("Round 68")
    time.sleep((8.44+10)/3)
    # Round 69
    pyautogui.press("space")
    print("Round 69")
    time.sleep((42.13+10)/3)
    # Round 70
    pyautogui.press("space")
    print("Round 70")
    time.sleep((41.14+10)/3)
    # Round 71
    pyautogui.press("space")
    print("Round 71")
    time.sleep((16.55+10)/3)
    # Round 72
    pyautogui.press("space")
    print("Round 72")
    time.sleep((21.70+10)/3)
    # Round 73
    pyautogui.press("space")
    print("Round 73")
    time.sleep((26.95+10)/3)
    # Round 74
    pyautogui.press("space")
    print("Round 74")
    time.sleep((82.39+10)/3)
    # Round 75
    pyautogui.press("space")
    print("Round 75")
    time.sleep((22.59+10)/3)
    # Round 76
    pyautogui.press("space")
    print("Round 76")
    time.sleep((1.78+10)/3)
    # Round 77
    pyautogui.press("space")
    print("Round 77")
    time.sleep((58.92+10)/3)
    # Round 78
    pyautogui.press("space")
    print("Round 78")
    time.sleep((90.00+10)/3)
    # Round 79
    pyautogui.press("space")
    print("Round 79")
    time.sleep((60.00+10)/3)
    # Round 80
    pyautogui.press("space")
    print("Round 80")
    time.sleep((2.00+10)/3)
    # Round 81
    pyautogui.press("space")
    print("Round 81")
    time.sleep((26.47+10)/3)
    # Round 82
    pyautogui.press("space")
    print("Round 82")
    time.sleep((35.68+10)/3)
    # Round 83
    pyautogui.press("space")
    print("Round 83")
    time.sleep((60.20+10)/3)
    # Round 84
    pyautogui.press("space")
    print("Round 84")
    time.sleep((25.00+10)/3)
    # Round 85
    pyautogui.press("space")
    print("Round 85")
    time.sleep((10.00+10)/3)
    # Round 86
    pyautogui.press("space")
    print("Round 86")
    time.sleep((20.85+10)/3)
    # Round 87
    pyautogui.press("space")
    print("Round 87")
    time.sleep((10.00+10)/3)
    # Round 88
    pyautogui.press("space")
    print("Round 88")
    time.sleep((14.55+10)/3)
    # Round 89
    pyautogui.press("space")
    print("Round 89")
    time.sleep((20.74+10)/3)
    # Round 90
    pyautogui.press("space")
    print("Round 90")
    time.sleep((11.90+10)/3)
    # Round 91
    pyautogui.press("space")
    print("Round 91")
    time.sleep((30.00+10)/3)
    # Round 92
    pyautogui.press("space")
    print("Round 92")
    time.sleep((35.00+10)/3)
    # Round 93
    pyautogui.press("space")
    print("Round 93")
    time.sleep((20.00+10)/3)
    # Round 94
    pyautogui.press("space")
    print("Round 94")
    time.sleep((15.00+10)/3)
    # Round 95
    pyautogui.press("space")
    print("Round 95")
    time.sleep((50.81+10)/3)
    # Round 96
    pyautogui.press("space")
    print("Round 96")
    time.sleep((32.12+10)/3)
    # Round 97
    pyautogui.press("space")
    print("Round 97")
    time.sleep((5.00+10)/3)
    # Round 98
    pyautogui.press("space")
    print("Round 98")
    time.sleep((30.00+10)/3)
    # Round 99
    pyautogui.press("space")
    print("Round 99")
    time.sleep((12.00+10)/3)
    # Round 100
    pyautogui.press("space")
    print("Round 100")
    time.sleep((0.10+10)/3)

if __name__ == "__main__":
    time.sleep(buffer)
    pyautogui.click(Pause)
    time.sleep(buffer)
    pyautogui.click(Restart)
    time.sleep(buffer)
    pyautogui.click(Confirm)
    time.sleep(buffer)
    Rounds()