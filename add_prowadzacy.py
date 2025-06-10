import json
import hashlib

def dodaj_prowadzacego(login, haslo, sciezka="users.json"):
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            users = json.load(f)
            if not isinstance(users, list):
                print("Plik users.json nie zawiera listy użytkowników, naprawiam...")
                users = []
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    if any(u["login"] == login for u in users):
        print("Użytkownik o takim loginie już istnieje!")
        return

    haslo_hash = hashlib.sha256(haslo.encode()).hexdigest()

    users.append({
        "login": login,
        "haslo_hash": haslo_hash,
        "rola": "prowadzacy"
    })

    with open(sciezka, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

    print(f"Konto prowadzącego '{login}' zostało dodane!")

dodaj_prowadzacego("PIO", "PIO")
