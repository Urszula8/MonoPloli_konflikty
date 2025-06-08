from pionek import Pionek


class Student:

    def __init__(self, nick, awatar):
        self.ects = 0
        self.nick = nick
        self.pionek = Pionek(awatar)
        # self.pionek.wybierzKolor(awatar)
