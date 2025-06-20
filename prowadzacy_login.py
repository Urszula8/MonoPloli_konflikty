import tkinter as tk
from tkinter import messagebox
import menu
import login_screen
from database import zaloguj_uzytkownika
import prowadzacy_window

def uruchom_logowanie_prowadzacy(prev_window):
    root = tk.Tk()
    root.title("Logowanie Prowadzącego")

    # Dynamiczne ustawienie rozmiaru okna na pełny ekran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
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

    root.bind('<Return>', lambda event: zaloguj())

    root.mainloop()

def powrot_do_menu(root):
    root.destroy()
    menu.main()
