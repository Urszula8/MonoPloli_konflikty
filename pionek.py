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

    def wybierzKolor(self,kolorPionka):
        self.kolor=kolorPionka

    def ruch(self,liczbaPol):
        if self.numerPola+liczbaPol>=LICZBA_POL:
            self.numerPola=self.numerPola+liczbaPol-LICZBA_POL
        else:
            self.numerPola=self.numerPola+liczbaPol


    def wyswietlPionek(self, plansza, ktoryPionek):
        plansza.pola[self.numerPola].tlo.create_image(12+pos[ktoryPionek][0], 18+pos[ktoryPionek][1], image=plansza.pola[self.numerPola].pionek[self.kolor])

