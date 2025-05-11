import tkinter as tk
from PIL import Image, ImageTk
import menu
import question_editor

def powrot_przycisk(okno):
    okno.destroy()
    menu.main()

def uruchom_okno_prowadzacy():
    okno = tk.Tk()
    okno.title("Okno Prowadzącego")
    okno.geometry("1920x1080")
    okno.configure(bg="#e2dbd8")

    # Przygotowanie grafiki przycisku powrotu
    powrot_img = Image.open("powrot.png").resize((210, 70))
    powrot_photo = ImageTk.PhotoImage(powrot_img)

    powrot_button = tk.Button(okno, image=powrot_photo, command=lambda: powrot_przycisk(okno), borderwidth=0)
    powrot_button.image = powrot_photo
    powrot_button.place(x=50, y=30)

    # Przycisk Edytuj bazę pytań
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

    okno.mainloop()