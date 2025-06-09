import tkinter as tk
from tkinter import messagebox

import login_screen
from database import zaloguj_uzytkownika
import lecturer_window

def uruchom_logowanie_prowadzacy(prev_window):
    prev_window.destroy()
    root = tk.Tk()
    root.title("Logowanie Prowadzącego")
    root.geometry("1920x1080")
    root.configure(bg="#e2dbd8")

    tk.Label(root, text="Login:").pack(pady=5)
    login_entry = tk.Entry(root)
    login_entry.pack()

    tk.Label(root, text="Hasło:").pack(pady=5)
    haslo_entry = tk.Entry(root, show="*")
    haslo_entry.pack()
