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
    "I love you", "Seni seviyorum", "Te amo", "Je t'aime", "Ich liebe dich", "Ti amo", "Eu te amo", "Я тебя люблю", "사랑해", "愛してる", "我爱你", "मुझे तुमसे प्यार है", "Σ' αγαπάω", "Ik hou van jou", "Jag älskar dig", "Kocham cię", "ฉันรักคุณ", "Anh yêu em", "Aku cinta kamu", "Я тебе кохаю"
]
_fonts = {}
def font_for(size):
  if size not in _fonts:
