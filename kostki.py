import tkinter as tk
from PIL import Image, ImageTk
import random

def zaladuj_grafiki_kostek():
    return [ImageTk.PhotoImage(Image.open(f"Kostka_{i}.png").resize((100, 100))) for i in range(1, 7)]

def stworz_labelki_kostek(okno, grafiki):
    label1 = tk.Label(okno, image=grafiki[0], bg="#e2dbd8")
    label2 = tk.Label(okno, image=grafiki[0], bg="#e2dbd8")
    label1.place(x=1100, y=200)
    label2.place(x=1250, y=200)
    return label1, label2


