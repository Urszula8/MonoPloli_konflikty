from PIL import Image, ImageTk
import tkinter as tk
import menu

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

    okno.mainloop()
