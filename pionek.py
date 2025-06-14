from PIL import Image, ImageTk
import tkinter as tk

PIONEK_X = 25
PIONEK_Y = 40
LICZBA_POL=38
pos=[[12,0],[36,0],[0,16],[24,16]]

class Pionek:
    kolor=0

    def __init__(self, kolor):
        self.kolor = kolor
        self.numerPola=0
        self.img_id = None

    def wybierzKolor(self,kolorPionka):
        self.kolor=kolorPionka

    def ruch(self, liczbaPol):
        poprzednie_pole = self.numerPola
        if self.numerPola + liczbaPol >= LICZBA_POL:
            self.numerPola = self.numerPola + liczbaPol - LICZBA_POL
        else:
            self.numerPola = self.numerPola + liczbaPol
        return poprzednie_pole

    def wyswietlPionek(self, plansza, ktoryPionek, stare_pole=None):
        if self.img_id and stare_pole is not None:
            plansza.pola[stare_pole].tlo.delete(self.img_id)

        self.img_id = plansza.pola[self.numerPola].tlo.create_image(
            12 + pos[ktoryPionek][0],
            18 + pos[ktoryPionek][1],
            image=plansza.pola[self.numerPola].pionek[self.kolor]
        )

    def animowany_ruch(self, plansza, ktoryPionek, liczbaPol, callback=None):
        kroki = []
        aktualne_pole = self.numerPola

        for i in range(1, liczbaPol + 1):
            pole = (aktualne_pole + i) % LICZBA_POL
            kroki.append(pole)

        def wykonaj_krok():
            if not kroki:
                if callback:
                    callback()
                return


