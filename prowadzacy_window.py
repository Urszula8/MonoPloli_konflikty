import tkinter as tk
from PIL import Image, ImageTk
import menu
import question_editor
import json
import os


def powrot_przycisk(okno):
    okno.destroy()
    menu.main()


def uruchom_okno_prowadzacy():
    if not os.path.exists("gra_status.json"):
        with open("gra_status.json", "w", encoding="utf-8") as f:
            json.dump({"status": "oczekiwanie", "gracze": []}, f)

    okno = tk.Tk()
    okno.title("Okno Prowadzącego")

    # Dynamiczne ustawienie rozmiaru okna na pełny ekran
    screen_width = okno.winfo_screenwidth()
    screen_height = okno.winfo_screenheight()
    okno.geometry(f"{screen_width}x{screen_height}")
    okno.configure(bg="#e2dbd8")

    # --- Przycisk powrotu
    powrot_img = Image.open("powrot.png").resize((210, 70))
    powrot_photo = ImageTk.PhotoImage(powrot_img)
    powrot_button = tk.Button(okno, image=powrot_photo, command=lambda: powrot_przycisk(okno), borderwidth=0)
    powrot_button.image = powrot_photo
    powrot_button.place(x=50, y=30)

    # --- Przycisk edycji pytań
    edytuj_button = tk.Button(
        okno,
        text="Edytuj bazę pytań",
        command=lambda: [okno.destroy(), question_editor.uruchom_edycje()],
        bg="#660000",
        fg="white",
        width=20,
        height=2
    )
    edytuj_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # --- Start gry
    def start_gra():
        try:
            with open("gra_status.json", "r", encoding="utf-8") as f:
                dane = json.load(f)
        except FileNotFoundError:
            dane = {}

        dane["status"] = "start"
        if "gracze" not in dane:
            dane["gracze"] = []

        with open("gra_status.json", "w", encoding="utf-8") as f:
            json.dump(dane, f, indent=2)

    tk.Button(okno, text="Start gry", command=start_gra).place(x=500, y=300)

    # --- Reset gry
    def reset_gra():
        with open("gra_status.json", "w", encoding="utf-8") as f:
            json.dump({"status": "oczekiwanie", "gracze": []}, f)

    tk.Button(okno, text="Reset gry", command=reset_gra).place(x=500, y=350)

    # --- Zamknięcie okna
    def on_closing():
        with open("gra_status.json", "w", encoding="utf-8") as f:
            json.dump({"status": "oczekiwanie", "gracze": []}, f)
        okno.destroy()

    okno.protocol("WM_DELETE_WINDOW", on_closing)

    # --- RANKING (tekst + aktualizacja)
    ranking_header = tk.Canvas(okno, width=227, height=50, bg="#750006", highlightthickness=0)
    ranking_header.place(x=50, y=200)
    ranking_header.create_text(113, 25, text="RANKING:", fill="white", font=('Inter', 20, 'bold'))

    # Lista rankingowa
    ranking_canvas = tk.Canvas(okno, width=227, height=450, bg="#750006", highlightthickness=0)
    ranking_canvas.place(x=50, y=250)

    def odswiez_ranking():
        try:
            with open("gra_status.json", "r", encoding="utf-8") as f:
                dane = json.load(f)
            gracze = sorted(dane.get("gracze", []), key=lambda x: -x["ects"])
            ranking_canvas.delete("all")
            for idx, g in enumerate(gracze):
                ranking_canvas.create_text(
                    113, 20 + idx * 30,
                    text=f"{g['login']}:  {g['ects']}",
                    fill="white",
                    font=("Arial", 14)
                )
        except Exception as e:
            print(f"[Błąd odświeżania rankingu]: {e}")

        okno.after(1000, odswiez_ranking)

    odswiez_ranking()

    okno.mainloop()
