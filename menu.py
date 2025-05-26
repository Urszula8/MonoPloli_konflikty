import tkinter as tk
from PIL import Image, ImageTk
import login_screen
import prowadzacy_window

def student_przycisk(root):
    root.destroy()
    login_screen.uruchom_ekran_logowania()

def prowadzacy_przycisk(root):
    root.destroy()
    prowadzacy_window.uruchom_okno_prowadzacy()

def main():
    root = tk.Tk()
    root.title("Menu Gry")
    root.geometry("1920x1080")
    root.configure(bg="#e2dbd8")

    # Wczytanie grafik
    logo_img = Image.open("logo.png").resize((600, 350))
    logo_photo = ImageTk.PhotoImage(logo_img)

    student_img = Image.open("student.png")
    student_photo = ImageTk.PhotoImage(student_img)

    prowadzacy_img = Image.open("prowadzacy.png")
    prowadzacy_photo = ImageTk.PhotoImage(prowadzacy_img)

    # Logo
    logo_label = tk.Label(root, image=logo_photo, bg="#e2dbd8")
    logo_label.image = logo_photo
    logo_label.pack(pady=30, padx=(30, 0))

    # Przycisk STUDENT
    student_button = tk.Button(root, image=student_photo, command=lambda: student_przycisk(root), borderwidth=0)
    student_button.image = student_photo
    student_button.pack(pady=10)

    # Przycisk PROWADZĄCY
    prowadzacy_button = tk.Button(root, image=prowadzacy_photo, command=lambda: prowadzacy_przycisk(root), borderwidth=0)
    prowadzacy_button.image = prowadzacy_photo
    prowadzacy_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
