import math as m
import random as r
import turtle as t
import tkinter.font as tkf

SC = 21
OY = 20
DURATION = 10
TICK = 16
ANIM = 42
LIFT = 34
GAP = 7 
SIZES = (9, 10, 11, 12)
FONT = "Arial"
BG = "#060208"

s = t.Screen()
s.setup(800, 800)
s.bgcolor(BG)
s.title("Love Heart")
s.tracer(0)

cv = s.getcanvas()
rng = r.Random(11)

PHRASES = [
    "I love you", "Seni seviyorum", "Te amo", "Je t'aime", 
    "Ich liebe dich", "Ti amo", "Eu te amo", "Я тебя люблю", 
    "사랑해", "愛してる", "我爱你", "मुझे तुमसे प्यार है", 
    "Σ' αγαπάω", "Ik hou van jou", "Jag älskar dig", "Kocham cię", 
    "ฉันรักคุณ", "Anh yêu em", "Aku cinta kamu", "Я тебе кохаю"
]

_fonts = {}


def font_for(size):
  if size not in _fonts:
      _fonts[size] = tkf.Font(
          root=cv, family=FONT, size=size, weight="bold"
      )
  return _fonts[size]


def heart(a):
    x = 16 * (m.sin(a) ** 3)
    y = (
        13 * m.cos(a)
        - 5 * m.cos(2 * a)
        - 2 * m.cos(3 * a)
        - m.cos(4 * a)
    )
    return x * SC, y * SC + OY


def hx(c):
    return "#02x%02x%02x" % tuple(
        int(max(0, min(1, v)) * 255) for v in c
    )


def 
