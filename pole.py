import tkinter as tk
from PIL import Image, ImageTk
import plansza
from plansza import *


class Pole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filename = "logo.png"
        self.wlasciwosc = None
        obraz = Image.open(self.filename).resize((plansza.POLE_X, plansza.POLE_Y))
        self.photo = ImageTk.PhotoImage(obraz)