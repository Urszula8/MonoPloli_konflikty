import tkinter as tk
from tkinter import messagebox
from database import zarejestruj_uzytkownika
import login_screen

def uruchom_rejestracje(prev_window):
    prev_window.destroy()
    root = tk.Tk()
    root.title("Rejestracja")

    # Dynamiczne dopasowanie rozmiaru okna
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(bg="#e2dbd8")

    tk.Label(root, text="Nowy login:").pack(pady=5)
    login_entry = tk.Entry(root)
    login_entry.pack()

    tk.Label(root, text="Hasło:").pack(pady=5)
    haslo_entry = tk.Entry(root, show="*")
    haslo_entry.pack()

    tk.Label(root, text="Powtórz hasło:").pack(pady=5)
    haslo2_entry = tk.Entry(root, show="*")
    haslo2_entry.pack()

    def zarejestruj():
        login = login_entry.get()
        haslo = haslo_entry.get()
        haslo2 = haslo2_entry.get()

        if haslo != haslo2:
            messagebox.showerror("Błąd", "Hasła się nie zgadzają")
            return

        if zarejestruj_uzytkownika(login, haslo, rola="student"):
            messagebox.showinfo("Sukces", "Rejestracja zakończona")
            root.destroy()
            login_screen.uruchom_ekran_logowania()
        else:
            messagebox.showerror("Błąd", "Użytkownik już istnieje")

    tk.Button(root, text="Zarejestruj", command=zarejestruj).pack(pady=10)
    tk.Button(root, text="Powrót", command=lambda: powrot_do_ekranu_wyboru(root)).pack(pady=10)

    root.bind('<Return>', lambda event: zarejestruj())

    root.mainloop()

def powrot_do_ekranu_wyboru(current_root):
    current_root.destroy()
    login_screen.uruchom_ekran_logowania()
