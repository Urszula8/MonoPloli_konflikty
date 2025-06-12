import tkinter as tk
from tkinter import messagebox

def pokaz_pytanie(okno_glowne, pytanie, on_close=None):
    popup = tk.Toplevel(okno_glowne)
    popup.title("Pytanie")
    popup.geometry("500x300")
    popup.configure(bg="#f4f4f4")

    tk.Label(popup, text=pytanie['text'], wraplength=450, bg="#f4f4f4", font=('Arial', 12)).pack(pady=10)

    if pytanie['type'] == "Sesja egzaminacyjna":
        for opt in pytanie['options'].split(', '):
            tk.Button(
                popup,
                text=opt,
                command=lambda o=opt: zamknij_popup(popup, o, pytanie['correct'], on_close)
            ).pack(pady=3)
    else:
        entry = tk.Entry(popup, font=('Arial', 12))
        entry.pack(pady=10)

        def zatwierdz():
            user_input = entry.get().strip()
            zamknij_popup(popup, user_input, pytanie['correct'], on_close)

        tk.Button(popup, text="Zatwierdź", command=zatwierdz).pack(pady=10)

def zamknij_popup(popup, odpowiedz, poprawna, on_close):
    if odpowiedz:
        if odpowiedz.lower() == poprawna.lower():
            messagebox.showinfo("Wynik", "Dobra odpowiedź!")
        else:
            messagebox.showinfo("Wynik", f"Zła odpowiedź.\nPoprawna: {poprawna}")
    else:
        messagebox.showinfo("Wynik", f"Brak odpowiedzi.\nPoprawna: {poprawna}")

    popup.destroy()
    if on_close:
        on_close()
