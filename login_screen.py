import tkinter as tk
from login import uruchom_logowanie
from register import uruchom_rejestracje
import menu

def uruchom_ekran_logowania():
    root = tk.Tk()
    root.title("Panel logowania studenta")

    # Automatyczne ustawienie rozmiaru okna do rozdzielczości ekranu
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(bg="#e2dbd8")

    tk.Label(root, text="Witaj, Studencie!", font=("Arial", 18), bg="#e2dbd8").pack(pady=20)

    tk.Button(root, text="Zaloguj się", command=lambda: uruchom_logowanie(root), width=20).pack(pady=10)
    tk.Button(root, text="Załóż konto", command=lambda: uruchom_rejestracje(root), width=20).pack(pady=10)

    tk.Button(root, text="Powrót do menu głównego", command=lambda: powrot_do_menu(root), width=25).pack(pady=20)

    root.mainloop()

def powrot_do_menu(root):
    root.destroy()
    menu.main()
