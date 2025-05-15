from PIL import Image, ImageTk
import tkinter as tk
import menu
from pole import *

def powrot_przycisk(okno):
    okno.destroy()
    menu.main()
def uruchom_okno_student():
    okno = tk.Tk()
    okno.title("Okno Studenta")
    okno.geometry("1920x1080")
    okno.configure(bg="#e2dbd8")

    # Przygotowanie grafiki przycisku
    powrot_img = Image.open("powrot.png").resize((210, 70))
    powrot_photo = ImageTk.PhotoImage(powrot_img)

    powrot_button = tk.Button(okno, image=powrot_photo, command=lambda: powrot_przycisk(okno), borderwidth=0)
    powrot_button.image = powrot_photo
    powrot_button.place(x=50, y=30)

    #przygotowanie tla do wyswietlania liczby punktow ECTS
    ectsy_tlo = tk.Canvas(okno, width=210, height=70, bg="#750006")
    ectsy_tlo.place(x=50, y=120)
    ectsy_text=ectsy_tlo.create_text(105,35,text="ECTSY: ",fill="white",font=('Inter 25'))

    # Wczytanie logo
    logo_img = Image.open("logo2.png").resize((800, 700))
    logo_photo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(okno, image=logo_photo, bg="#e2dbd8")
    logo_label.image = logo_photo
    logo_label.place(x=300,y=-250)

    #przygotowanie ekranu ładowania
    ladowanie_tlo = tk.Canvas(okno, width=450, height=330, bg="#f3eee6")
    ladowanie_tlo.place(x=520, y=220)
    ladowanie_text = ladowanie_tlo.create_text(250, 50, text="Oczekiwanie aż\nprowadzący zacznie grę", fill="black", font=('Inter 25'))

    #przygotowanie tła do wyświetlania rankingu
    ranking_tlo = tk.Canvas(okno, width=210, height=500, bg="#750006")
    ranking_tlo.place(x=50, y=200)
    ranking_text = ranking_tlo.create_text(105,35,text="RANKING: ",fill="white",font=('Inter 25'))

    #przygotowanie pól
    pole1=Pole(1,2)
    pola_gora = [Pole(POLE_X * (i+1)+350, 150) for i in range(0,10)]
    pola_dol = [Pole(POLE_X * (i+1)+350, POLE_Y+500) for i in range(0,10)]
    pola_lewo = [Pole(350, POLE_Y * i+150) for i in range(0, 9)]
    pola_prawo = [Pole(POLE_X*11+350, POLE_Y * i+150) for i in range(0, 9)]

    pola = pola_gora + pola_dol + pola_lewo + pola_prawo
    pola_tlo = [tk.Canvas(okno, width=POLE_X, height=POLE_Y, bg="green") for i in pola]
    for i in range(0,len(pola)):
        pola_tlo[i].place(x=pola[i].x, y=pola[i].y)







    okno.mainloop()
