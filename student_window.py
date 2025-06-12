from PIL import Image, ImageTk
import tkinter as tk
import menu
import json
from nieobecnosc import *
from plansza import *
from student import Student
import question_popup 
import threading
import time
import os

def powrot_przycisk(okno):
    okno.destroy()
    menu.main()

def uruchom_okno_student(login):
    okno = tk.Tk()
    gracz = Student(login, 0)
    okno.title("Okno Studenta")
    okno.geometry("1920x1080")
    okno.configure(bg="#e2dbd8")
    
    
    # Przygotowanie grafiki przycisku
    powrot_img = Image.open("powrot.png").resize((210, 70))
    powrot_photo = ImageTk.PhotoImage(powrot_img)
    powrot_button = tk.Button(okno, image=powrot_photo, command=lambda: powrot_przycisk(okno), borderwidth=0)
    powrot_button.image = powrot_photo
    powrot_button.place(x=50, y=30)

    # przygotowanie tla do wyswietlania liczby punktow ECTS
    ectsy_tlo = tk.Canvas(okno, width=210, height=70, bg="#750006")
    ectsy_tlo.place(x=50, y=120)
    ectsy_tlo.create_text(105, 35, text="ECTSY: ", fill="white", font='Inter 25')

    # Wczytanie logo
    logo_img = Image.open("logo2.png").resize((800, 700))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(okno, image=logo_photo, bg="#e2dbd8")
    logo_label.image = logo_photo
    logo_label.place(x=300, y=-280)

    # przygotowanie ekranu ładowania
    ladowanie_tlo = tk.Canvas(okno, width=450, height=330, bg="#f3eee6")
    ladowanie_tlo.place(x=520, y=220)
    ladowanie_tlo.create_text(250, 50, text="Oczekiwanie aż\nprowadzący zacznie grę", fill="black",
                              font='Inter 25')

    # przygotowanie tła do wyświetlania rankingu
    ranking_tlo = tk.Canvas(okno, width=210, height=500, bg="#750006")
    ranking_tlo.place(x=50, y=200)
    
    # przygotowanie pól
    plansza_do_gry = Plansza(okno, 11, 8, 100, 400, 70, 50)
    plansza_do_gry.WypelnijDomyslnie()
    plansza_do_gry.Rysuj()

    # umieszczenie pionka gracza na polu startowym
    gracz.pionek.wyswietlPionek(plansza_do_gry, 0)

    # === ŁADOWANIE PYTAŃ ===
    with open("baza_pytan.json", "r", encoding="utf-8") as f:
        wszystkie_pytania = json.load(f)
    pytania_wiedza = [p for p in wszystkie_pytania if p["type"] == "Sprawdzenie wiedzy"]
    pytania_sesja = [p for p in wszystkie_pytania if p["type"] == "Sesja egzaminacyjna"]

    # === FUNKCJA: sprawdzenie pola i pytanie ===
    def sprawdz_pole():
        pole = plansza_do_gry.pola[gracz.pionek.numerPola]
        typ = type(pole).__name__

        if typ == "SprawdzenieWiedzy" and pytania_wiedza:
            pytanie = pytania_wiedza.pop(0)
            question_popup.pokaz_pytanie(okno, pytanie, gracz)
        elif typ == "SesjaEgzaminacyjna" and pytania_sesja:
            pytanie = pytania_sesja.pop(0)
            question_popup.pokaz_pytanie(okno, pytanie, gracz)
    def rusz_o_jedno_pole():
        gracz.pionek.numerPola = (gracz.pionek.numerPola + 1) % len(plansza_do_gry.pola)
        gracz.pionek.wyswietlPionek(plansza_do_gry, gracz.pionek.numerPola)
        sprawdz_pole()
    # === TYM PRZYCISK: testuj pytanie ===
    
    tk.Button(okno, text="Rusz o 1 pole", command=rusz_o_jedno_pole).place(x=900, y=700)
    tk.Button(okno, text="Sprawdź pole (test)", command=sprawdz_pole).place(x=900, y=750)

    okno.mainloop()

