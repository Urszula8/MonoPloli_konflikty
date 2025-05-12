import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import json
import prowadzacy_window

# Główna funkcja uruchamiająca edytor pytań

def uruchom_edycje():
    edytor = tk.Tk()
    edytor.title("Edycja Bazy Pytań")
    edytor.geometry("1000x750")
    edytor.configure(bg="#f2f2f2")

    questions = []  # Lista przechowująca pytania jako słowniki

    # Tabela do wyświetlania pytań
    tree = ttk.Treeview(edytor, columns=('Treść', 'Typ', 'Odpowiedzi', 'Poprawna'), show='headings')
    tree.heading('Treść', text='Treść pytania')
    tree.heading('Typ', text='Typ')
    tree.heading('Odpowiedzi', text='Odpowiedzi')
    tree.heading('Poprawna', text='Poprawna odpowiedź')
    tree.pack(fill=tk.BOTH, expand=True, pady=10)

    # Pola do wprowadzenia danych
    entry_question = tk.Entry(edytor, width=70)
    entry_question.pack(pady=5)

    combo_type = ttk.Combobox(edytor, values=["Sprawdzenie wiedzy", "Sesja egzaminacyjna"])
    combo_type.pack(pady=5)

    entry_correct = tk.Entry(edytor, width=70)
    entry_correct.pack(pady=5)

    # Instrukcja pod polami
    label_help = tk.Label(
        edytor,
        text="Dla 'Sprawdzenie wiedzy' wpisz jedną odpowiedź jako poprawną.\nDla 'Sesja egzaminacyjna' otworzy się dodatkowe okno do wpisania 4 opcji i poprawnej litery (A/B/C/D).",
        bg="#f2f2f2",
        fg="gray"
    )
    label_help.pack(pady=2)

    # Okno dla wpisania odpowiedzi zamkniętych A/B/C/D
    def otworz_okno_opcji():
        top = tk.Toplevel(edytor)
        top.title("Opcje odpowiedzi")

        labels = ['A', 'B', 'C', 'D']
        entries = {}

        for i, lit in enumerate(labels):
            tk.Label(top, text=f"{lit})").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(top, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries[lit] = entry

        tk.Label(top, text="Poprawna litera (A/B/C/D):").grid(row=4, column=0, columnspan=2, pady=10)
        correct_var = tk.Entry(top, width=5)
        correct_var.grid(row=5, column=0, columnspan=2)

        # Zapisanie pytań po zamknięciu okna
        def save_and_close():
            options_text = ", ".join([f"{lit}) {entries[lit].get().strip()}" for lit in labels])
            correct = correct_var.get().strip().upper()
            if correct not in labels:
                messagebox.showerror("Błąd", "Poprawna odpowiedź musi być A, B, C lub D")
                return
            top.destroy()
            dodaj_pytanie(options_text, correct)

        tk.Button(top, text="Zapisz", command=save_and_close).grid(row=6, column=0, columnspan=2, pady=10)

    # Funkcja dodająca pytanie do listy i tabeli
    def dodaj_pytanie(options, correct):
        text = entry_question.get().strip()
        qtype = combo_type.get().strip()
        if text and qtype and correct:
            tree.insert('', 'end', values=(text, qtype, options, correct))
            questions.append({'text': text, 'type': qtype, 'options': options, 'correct': correct})
            entry_question.delete(0, tk.END)
            entry_correct.delete(0, tk.END)
            combo_type.set('')
        else:
            messagebox.showwarning("Błąd", "Uzupełnij wszystkie pola")

    # Obsługa przycisku "Dodaj pytanie"
    def add_question():
        qtype = combo_type.get().strip()
        if qtype == "Sesja egzaminacyjna":
            otworz_okno_opcji()
        else:
            text = entry_question.get().strip()
            correct = entry_correct.get().strip()
            if text and qtype and correct:
                tree.insert('', 'end', values=(text, qtype, '', correct))
                questions.append({'text': text, 'type': qtype, 'options': '', 'correct': correct})
                entry_question.delete(0, tk.END)
                entry_correct.delete(0, tk.END)
                combo_type.set('')
            else:
                messagebox.showwarning("Błąd", "Uzupełnij wszystkie pola")

    # Zapis danych do pliku JSON
    def save_to_file():
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if path:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(questions, f, ensure_ascii=False, indent=2)

    # Wczytanie danych z pliku JSON
    def load_from_file():
        path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if path:
            with open(path, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
            questions.clear()
            questions.extend(loaded)
            tree.delete(*tree.get_children())
            for q in questions:
                tree.insert('', 'end', values=(q['text'], q['type'], q.get('options', ''), q.get('correct', '')))

    # Usuwanie zaznaczonego pytania
    def delete_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Zaznacz pytanie do usunięcia")
            return
        for item in selected:
            values = tree.item(item, 'values')
            tree.delete(item)
            questions[:] = [q for q in questions if q['text'] != values[0]]

    # Przyciski funkcyjne
    tk.Button(edytor, text="Dodaj Pytanie", command=add_question).pack(pady=5)
    tk.Button(edytor, text="Zapisz do pliku", command=save_to_file).pack(pady=5)
    tk.Button(edytor, text="Wczytaj z pliku", command=load_from_file).pack(pady=5)
    tk.Button(edytor, text="Usuń zaznaczone pytanie", command=delete_selected).pack(pady=5)
    tk.Button(edytor, text="Powrót", command=lambda: [edytor.destroy(), prowadzacy_window.uruchom_okno_prowadzacy()]).pack(pady=10)

    edytor.mainloop()
