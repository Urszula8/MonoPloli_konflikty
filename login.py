import tkinter as tk
from database import zaloguj_uzytkownika
import student_window
import login_screen

def uruchom_logowanie(prev_window):
    prev_window.destroy()
    root = tk.Tk()
    root.title("Logowanie")
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
        if zaloguj_uzytkownika(login, haslo):
            messagebox.showinfo("Sukces", "Zalogowano pomyślnie!")
            root.destroy()
            student_window.uruchom_okno_student(login)
        else:
            messagebox.showerror("Błąd", "Nieprawidłowy login lub hasło")

    tk.Button(root, text="Zaloguj", command=zaloguj).pack(pady=10)
    tk.Button(root, text="Powrót", command=lambda: powrot_do_ekranu_wyboru(root)).pack(pady=10)

    root.mainloop()

def powrot_do_ekranu_wyboru(current_root):
    current_root.destroy()
    login_screen.uruchom_ekran_logowania()
