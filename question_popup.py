import tkinter as tk
from tkinter import messagebox
import json
from functools import partial

def aktualizuj_ects(login, punkty):
    try:
        with open("gra_status.json", "r", encoding="utf-8") as f:
            dane = json.load(f)
        for g in dane["gracze"]:
            if g["login"].lower() == login.lower():
                g["ects"] = punkty
                break
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
                command=lambda o=opt: zamknij_popup(popup, o, pytanie['correct'], gracz, okno_glowne, on_close, pytanie['type'])

            ).pack(pady=3)
    else:
        entry = tk.Entry(popup, font=('Arial', 12))
        entry.pack(pady=10)

        def zatwierdz():
            user_input = entry.get().strip()
            zamknij_popup(popup, user_input, pytanie['correct'], gracz, okno_glowne, on_close, pytanie['type'])


        tk.Button(popup, text="Zatwierdź", command=zatwierdz).pack(pady=10)

def zamknij_popup(popup, odpowiedz, poprawna, gracz, okno_glowne, on_close, typ_pytania):
    popup.destroy()

    if not gracz:
        return

    # Rozpoznanie poprawności odpowiedzi
    if poprawna.strip().startswith(("A", "B", "C", "D")):
        odp_litera = odpowiedz.strip().split(")")[0].upper()
        poprawna_litera = poprawna.strip().split(")")[0].upper()
        poprawna_odpowiedz = odp_litera == poprawna_litera
    else:
        poprawna_odpowiedz = odpowiedz.strip().lower() == poprawna.strip().lower()

    # Punkty i wynik
    if poprawna_odpowiedz:
        messagebox.showinfo("Wynik", "Dobra odpowiedź!")
        gracz.ects += 1
        aktualizuj_ects(gracz.login, gracz.ects)

        if typ_pytania == "Sesja egzaminacyjna":
            if not hasattr(gracz, "sesja_counter"):
                gracz.sesja_counter = 1
            else:
                gracz.sesja_counter += 1

            if not hasattr(gracz, "punkty_sesji"):
                gracz.punkty_sesji = 1
            else:
                gracz.punkty_sesji += 1

            # Kontynuacja sesji
            if hasattr(gracz, "pytania_sesja") and gracz.pytania_sesja and gracz.sesja_counter < 3:
                kolejne = gracz.pytania_sesja.pop(0)
                pokaz_pytanie(okno_glowne, kolejne, gracz, on_close)
                return
            else:
                messagebox.showinfo("Sesja zakończona", f"Zakończono sesję egzaminacyjną.\nZdobyte w sesji: {gracz.punkty_sesji} ECTS.")
                gracz.sesja_counter = 0
                gracz.punkty_sesji = 0
    else:
        messagebox.showinfo("Wynik", f"Zła odpowiedź.\nPoprawna: {poprawna}")
        if typ_pytania == "Sesja egzaminacyjna":
            messagebox.showinfo("Sesja zakończona", f"Zakończono sesję egzaminacyjną.\nZdobyte w sesji: {getattr(gracz, 'punkty_sesji', 0)} ECTS.")
            gracz.sesja_counter = 0
            gracz.punkty_sesji = 0

    if on_close:
        on_close()
