import json
import os
import hashlib

DB_FILE = "users.json"

def _load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({}, f)
    with open(DB_FILE, "r") as f:
        return json.load(f)

def _save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

import json
import hashlib

def zarejestruj_uzytkownika(login, haslo, rola="student", sciezka="users.json"):
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    if any(u["login"] == login for u in users):
        return False  # Użytkownik już istnieje

    haslo_hash = hashlib.sha256(haslo.encode()).hexdigest()

    users.append({
        "login": login,
        "haslo_hash": haslo_hash,
        "rola": rola
    })

    with open(sciezka, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

    return True


def zaloguj_uzytkownika(login, haslo, rola, sciezka="users.json"):
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            users = json.load(f)
    except FileNotFoundError:
        return False

    haslo_hash = hashlib.sha256(haslo.encode()).hexdigest()

    for user in users:
        if user["login"] == login and user["haslo_hash"] == haslo_hash and user["rola"] == rola:
            return True
    return False

