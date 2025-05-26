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

def zarejestruj_uzytkownika(login, haslo):
    data = _load_db()
    if login in data:
        return False
    data[login] = hash_password(haslo)
    _save_db(data)
    return True

def zaloguj_uzytkownika(login, haslo):
    data = _load_db()
    return login in data and data[login] == hash_password(haslo)
