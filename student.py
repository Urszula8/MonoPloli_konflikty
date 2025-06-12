from pionek import Pionek


class Student:

    def __init__(self, login, awatar):
        self.ects = 0
        self.login = login
        self.pionek = Pionek(awatar)
        # self.pionek.wybierzKolor(awatar)
