import tkinter as tk
from PIL import Image, ImageTk
import random
def zaladuj_grafiki_kostek():
    return [ImageTk.PhotoImage(Image.open(f"Kostka_{i}.png").resize((100, 100))) for i in range(1, 7)]
