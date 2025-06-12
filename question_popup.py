import tkinter as tk
from tkinter import messagebox
import json
def aktualizuj_ects(login, punkty):
        try:
            with open("gra_status.json", "r", encoding="utf-8") as f:
                dane = json.load(f)
            for g in dane["gracze"]:
                if g["login"].lower() == login.lower():
                    g["ects"] = punkty
                    break
            print("[DEBUG] Dane przed zapisem:", json.dumps(dane, indent=2))
            with open("gra_status.json", "w", encoding="utf-8") as f:
                json.dump(dane, f, indent=2)
        except:
            pass
def pokaz_pytanie(okno_glowne, pytanie, gracz=None, on_close=None):
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
                command=lambda o=opt: zamknij_popup(popup, o, pytanie['correct'], gracz, on_close)
            ).pack(pady=3)
    else:
        entry = tk.Entry(popup, font=('Arial', 12))
        entry.pack(pady=10)

        def zatwierdz():
            user_input = entry.get().strip()
            zamknij_popup(popup, user_input, pytanie['correct'], gracz, on_close)

        tk.Button(popup, text="Zatwierdź", command=zatwierdz).pack(pady=10)


def zamknij_popup(popup, odpowiedz, poprawna, gracz, on_close):
    if odpowiedz:
        if odpowiedz.lower() == poprawna.lower():
            messagebox.showinfo("Wynik", "Dobra odpowiedź!")
            if gracz:
                print(f"AKTUALIZUJ: {gracz.login} -> {gracz.ects}")
                gracz.ects += 1
                try:
                    print(">>> ZAPISUJE PUNKT DO JSON")
                    aktualizuj_ects(gracz.login, gracz.ects)
                except:
                    pass
        else:
            messagebox.showinfo("Wynik", f"Zła odpowiedź.\nPoprawna: {poprawna}")
    else:
        messagebox.showinfo("Wynik", f"Brak odpowiedzi.\nPoprawna: {poprawna}")

    popup.destroy()
    if on_close:
        on_close()
