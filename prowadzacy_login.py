import tkinter as tk
from tkinter import messagebox

import login_screen
from database import zaloguj_uzytkownika
import prowadzacy_window

def uruchom_logowanie_prowadzacy(prev_window):
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

    def zaloguj():
        login = login_entry.get()
        haslo = haslo_entry.get()
        if zaloguj_uzytkownika(login, haslo, rola="prowadzacy"):
            messagebox.showinfo("Sukces", "Zalogowano jako prowadzący!")
            root.destroy()
            prowadzacy_window.uruchom_okno_prowadzacy()
        else:
            messagebox.showerror("Błąd", "Nieprawidłowy login lub hasło")

    tk.Button(root, text="Zaloguj", command=zaloguj).pack(pady=10)
    tk.Button(root, text="Powrót", command=lambda: powrot_do_menu(root)).pack(pady=10)

    root.mainloop()

def powrot_do_ekranu_wyboru(current_root):
    current_root.destroy()
    login_screen.uruchom_ekran_logowania()
