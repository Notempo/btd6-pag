# Use Geraldo as hero
# Play on Cubism (Easy, Standard)
# Turn off Autostart

import pyautogui as pag
import time as t

p = 0.2
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
h7 = (1563,74)
h8 = (1563,218)
h9 = (1563,360)
h10 = (1563,501)
h11 = (1401,67)
h12 = (1400,229)
h13 = (1237,81)
h14 = (1237,227)
h15 = (594,1009)
h16 = (757,1010)
h17 = (552,864)
h18 = (1401,383)
h19 = (1400,532)
h20 = (1070,80)

def Rounds():
    # Round 1
    for i in range(2):
        pag.press("space")
        t.sleep(p)
    print("Round 1")
    pag.press("u")
    t.sleep(p)
    pag.moveTo(u1)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.press("q")
    t.sleep(p)
    pag.moveTo(q1)
    t.sleep(p)
    pag.click()
    t.sleep((17.51+0)/3)
    # Round 2
    pag.press("space")
    print("Round 2")
    t.sleep((19.00+3)/3)
    # Round 3
    pag.press("space")
    print("Round 3")
    t.sleep((16.71+3)/3)
    # Round 4
    pag.press("space")
    print("Round 4")
    t.sleep((17.31+3)/3)
    # Round 5
    pag.press("space")
    print("Round 5")
    t.sleep((16.50+4)/3)
    # Round 6
    pag.press("space")
    print("Round 6")
    pag.press("u")
    t.sleep(p)
    pag.click(Shop)
    t.sleep(p)
    pag.click(nft1)
    t.sleep(p)
    pag.moveTo(nft2)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(Shop)
    t.sleep(p)
    pag.click(esc)
    t.sleep((18.70+0)/3)
    # Round 7
    pag.press("space")
    print("Round 7")
    t.sleep((26.80+4)/3)
    # Round 8
    pag.press("space")
    print("Round 8")
    t.sleep((28.87+10)/3)
    # Round 9
    pag.press("space")
    print("Round 9")
    t.sleep((18.95+11)/3)
    # Round 10
    pag.press("space")
    print("Round 10")
    t.sleep((47.99+10)/3)
    # Round 11
    pag.press("space")
    print("Round 11")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h1)
    t.sleep(p)
    pag.click()
    t.sleep((19.16+5)/3)
    # Round 12
    pag.press("space")
    print("Round 12")
    t.sleep((17.39+10)/3)
    # Round 13
    pag.press("space")
    print("Round 13")
    pag.click(h1)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep((32.21+9)/3)
    # Round 14
    pag.press("space")
    print("Round 14")
    pag.click(h1)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep((26.63+10)/3)
    # Round 15
    pag.press("space")
    print("Round 15")
    pag.press("r")
    t.sleep(p)
    pag.moveTo(r1)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(esc)
    t.sleep((25.00+8)/3)
    # Round 16
    pag.press("space")
    print("Round 16")
    pag.click(r1)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep((16.02+5)/3)
    # Round 17
    pag.press("space")
    print("Round 17")
    t.sleep((5.00+10)/3)
    # Round 18
    pag.press("space")
    print("Round 18")
    t.sleep((26.82+10)/3)
    # Round 19
    pag.press("space")
    print("Round 19")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h2)
    t.sleep(p)
    pag.click()
    t.sleep((15.76+5)/3)
    # Round 20
    pag.press("space")
    print("Round 20")
    pag.click(h2)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep((5.25+10)/3)
    # Round 21
    pag.press("space")
    print("Round 21")
    pag.click(h2)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(r1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep((18.12+5)/3)
    # Round 22
    pag.press("space")
    print("Round 22")
    t.sleep((8.00+10)/3)
    # Round 23
    pag.press("space")
    print("Round 23")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h3)
    t.sleep(p)
    pag.click()
    t.sleep((6.82+10)/3)
    # Round 24
    pag.press("space")
    print("Round 24")
    pag.click(h3)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep((9.00+20)/3)
    # Round 25
    pag.press("space")
    print("Round 25")
    t.sleep((21.14+10)/3)
    # Round 26
    pag.press("space")
    print("Round 26")
    pag.press("k")
    t.sleep(p)
    pag.moveTo(k1)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(k1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep((14.51+8)/3)
    # Round 27
    pag.press("space")
    print("Round 27")
    pag.click(k1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep((34.26+8)/3)
    # Round 28
    pag.press("space")
    print("Round 28")
    pag.click(h1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("f")
    t.sleep(p)
    pag.moveTo(f1)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((5.00+13)/3)
    # Round 29
    pag.press("space")
    print("Round 29")
    pag.click(h2)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((15.25+5)/3)
    # Round 30
    pag.press("space")
    print("Round 30")
    pag.click(h3)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(f1)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((13.07+8)/3)
    # Round 31
    pag.press("space")
    print("Round 31")
    pag.click(f1)
    t.sleep(p)
    pag.press(".")
    t.sleep(p)
    pag.press(".")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((15.91+5)/3)
    # Round 32
    pag.press("space")
    print("Round 32")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h4)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h4)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((27.96+5)/3)
    # Round 33
    pag.press("space")
    print("Round 33")
    pag.click(h4)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(q1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((25.34+5)/3)
    # Round 34
    pag.press("space")
    print("Round 34")
    pag.click(h4)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((36.00+5)/3)
    # Round 35
    pag.press("space")
    print("Round 35")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h5)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h5)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((33.76+5)/3)
    # Round 36
    pag.press("space")
    print("Round 36")
    pag.click(k1)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(h5)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((20.99+5)/3)
    # Round 37
    pag.press("space")
    print("Round 37")
    pag.click(h1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((43.51+10)/3)
    # Round 38
    pag.press("space")
    print("Round 38")
    pag.click(h2)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((29.06+12)/3)
    # Round 39
    pag.press("space")
    print("Round 39")
    pag.click(h3)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((37.93+15)/3)
    # Round 40
    pag.press("space")
    print("Round 40")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h6)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h6)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((1.00+20)/3)
    # Round 41
    pag.click(Next)
    t.sleep(1)
    pag.click(Freeplay)
    t.sleep(1)
    pag.click(OK)
    t.sleep(1)
    pag.press("space")
    print("Round 41")
    pag.click(r1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((46.20+10)/3)
    # Round 42
    pag.press("space")
    print("Round 42")
    pag.press("k")
    t.sleep(p)
    pag.moveTo(k2)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(k2)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(".")
    t.sleep(p)
    pag.press(".")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((11.60+10)/3)
    # Round 43
    pag.press("space")
    print("Round 43")
    pag.click(h4)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((9.26+10)/3)
    # Round 44
    pag.press("space")
    print("Round 44")
    pag.click(h5)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((23.67+10)/3)
    # Round 45
    pag.press("space")
    print("Round 45")
    t.sleep((53.10+10)/3)
    # Round 46
    pag.press("space")
    print("Round 46")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h7)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h7)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((7.00+10)/3)
    # Round 47
    pag.press("space")
    print("Round 47")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h8)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h8)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((24.65+10)/3)
    # Round 48
    pag.press("space")
    print("Round 48")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h9)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h9)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((55.72+10)/3)
    # Round 49
    pag.press("space")
    print("Round 49")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h10)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h10)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((50.00+10)/3)
    # Round 50
    pag.press("space")
    print("Round 50")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h11)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h11)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((28.98+10)/3)
    # Round 51
    pag.press("space")
    print("Round 51")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h12)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h12)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((24.14+10)/3)
    # Round 52
    pag.press("space")
    print("Round 52")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h13)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h13)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((20.56+10)/3)
    # Round 53
    pag.press("space")
    print("Round 53")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h14)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h14)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((35.00+10)/3)
    # Round 54
    pag.press("space")
    print("Round 54")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h15)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h15)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((19.41+10)/3)
    # Round 55
    pag.press("space")
    print("Round 55")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h16)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h16)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((29.78+20)/3)
    # Round 56
    pag.press("space")
    print("Round 56")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h17)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h17)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((16.18+20)/3)
    # Round 57
    pag.press("space")
    print("Round 57")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h18)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h18)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((26.23+20)/3)
    # Round 58
    pag.press("space")
    print("Round 58")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h19)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h19)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((43.98+20)/3)
    # Round 59
    pag.press("space")
    print("Round 59")
    pag.press("h")
    t.sleep(p)
    pag.moveTo(h20)
    t.sleep(p)
    pag.click()
    t.sleep(p)
    pag.click(h20)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press("esc")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((26.16+20)/3)
    # Round 60
    pag.press("space")
    print("Round 60")
    pag.click(f1)
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.press(",")
    t.sleep(p)
    pag.click(r1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((1.00+30)/3)
    # Round 61
    pag.press("space")
    print("Round 61")
    pag.click(h1)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((20.00+20)/3)
    # Round 62
    pag.press("space")
    print("Round 62")
    pag.click(h2)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((48.29+20)/3)
    # Round 63
    pag.press("space")
    print("Round 63")
    pag.click(h3)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((42.25+20)/3)
    # Round 64
    pag.press("space")
    print("Round 64")
    pag.click(h4)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((9.53+20)/3)
    # Round 65
    pag.press("space")
    print("Round 65")
    pag.click(h5)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    t.sleep((62.00+20)/3)
    # Round 66
    pag.press("space")
    print("Round 66")
    pag.click(h6)
    t.sleep(p)
    pag.press("/")
    t.sleep(p)
    pag.click(esc)
    t.sleep(p)
    pag.click(esc)
    return 0
    t.sleep((22.75+20)/3)
    # Round 67
    pag.press("space")
    print("Round 67")
    t.sleep((26.44+20)/3)
    # Round 68
    pag.press("space")
    print("Round 68")
    t.sleep((8.44+20)/3)
    # Round 69
    pag.press("space")
    print("Round 69")
    t.sleep((42.13+20)/3)
    # Round 70
    pag.press("space")
    print("Round 70")
    t.sleep((41.14+20)/3)
    # Round 71
    pag.press("space")
    print("Round 71")
    t.sleep((16.55+20)/3)
    # Round 72
    pag.press("space")
    print("Round 72")
    t.sleep((21.70+20)/3)
    # Round 73
    pag.press("space")
    print("Round 73")
    t.sleep((26.95+20)/3)
    # Round 74
    pag.press("space")
    print("Round 74")
    t.sleep((82.39+20)/3)
    # Round 75
    pag.press("space")
    print("Round 75")
    t.sleep((22.59+20)/3)
    # Round 76
    pag.press("space")
    print("Round 76")
    t.sleep((1.78+20)/3)
    # Round 77
    pag.press("space")
    print("Round 77")
    t.sleep((58.92+20)/3)
    # Round 78
    pag.press("space")
    print("Round 78")
    t.sleep((90.00+20)/3)
    # Round 79
    pag.press("space")
    print("Round 79")
    t.sleep((60.00+20)/3)
    # Round 80
    pag.press("space")
    print("Round 80")
    t.sleep((2.00+20)/3)
    # Round 81
    pag.press("space")
    print("Round 81")
    t.sleep((26.47+20)/3)
    # Round 82
    pag.press("space")
    print("Round 82")
    t.sleep((35.68+20)/3)
    # Round 83
    pag.press("space")
    print("Round 83")
    t.sleep((60.20+20)/3)
    # Round 84
    pag.press("space")
    print("Round 84")
    t.sleep((25.00+20)/3)
    # Round 85
    pag.press("space")
    print("Round 85")
    t.sleep((10.00+20)/3)
    # Round 86
    pag.press("space")
    print("Round 86")
    t.sleep((20.85+20)/3)
    # Round 87
    pag.press("space")
    print("Round 87")
    t.sleep((10.00+20)/3)
    # Round 88
    pag.press("space")
    print("Round 88")
    t.sleep((14.55+20)/3)
    # Round 89
    pag.press("space")
    print("Round 89")
    t.sleep((20.74+20)/3)
    # Round 90
    pag.press("space")
    print("Round 90")
    t.sleep((11.90+20)/3)
    # Round 91
    pag.press("space")
    print("Round 91")
    t.sleep((30.00+20)/3)
    # Round 92
    pag.press("space")
    print("Round 92")
    t.sleep((35.00+20)/3)
    # Round 93
    pag.press("space")
    print("Round 93")
    t.sleep((20.00+20)/3)
    # Round 94
    pag.press("space")
    print("Round 94")
    t.sleep((15.00+20)/3)
    # Round 95
    pag.press("space")
    print("Round 95")
    t.sleep((50.81+20)/3)
    # Round 96
    pag.press("space")
    print("Round 96")
    t.sleep((32.12+20)/3)
    # Round 97
    pag.press("space")
    print("Round 97")
    t.sleep((5.00+20)/3)
    # Round 98
    pag.press("space")
    print("Round 98")
    t.sleep((30.00+20)/3)
    # Round 99
    pag.press("space")
    print("Round 99")
    t.sleep((12.00+20)/3)
    # Round 100
    pag.press("space")
    print("Round 100")
    t.sleep((0.10+20)/3)

if __name__ == "__main__":
    t.sleep(p)
    pag.click(Pause)
    t.sleep(p)
    pag.click(Restart)
    t.sleep(p)
    pag.click(Confirm)
    t.sleep(p)
    Rounds()