from random import randint, choice


class Postac:  # podstawowa klasa wszystkich postaci
    def __init__(self, nazwa, zycie, maks_zycie) -> None:
        self.nazwa = nazwa
        self.zycie = zycie
        self.maks_zycie = maks_zycie

    def atakuj(self, przeciwnik):
        atak = randint(0, 3)

        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}.")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa} zadając {atak} obrażeń.")
            przeciwnik.zycie -= atak


class Gracz(Postac):
    def __init__(self, imie):
        super().__init__(imie, 10, 10)

    def walcz(self, przeciwnik):
        print(f"{self.nazwa} natrafił na {przeciwnik.nazwa}.")
        while True:
            print(f"HP gracza: {self.zycie}")
            print(f"HP {przeciwnik.nazwa}: {przeciwnik.zycie}")

            akcja = input("Co chcesz zrobić? (atakuj, uciekaj): ")

            if akcja == 'atakuj':
                self.atakuj(przeciwnik)
                przeciwnik.atakuj(self)
            elif akcja == 'uciekaj':
                print(f"{self.nazwa} ucieka!")
                break
            else:
                print("Nieprawidłowa akcja.")

            if przeciwnik.zycie == 0:
                print(f"{self.nazwa} wygrywa!")
                print(f"{przeciwnik.nazwa} jest pokonany.")
                break

            if self.zycie == 0:
                print(f"{self.nazwa} ginie!")
                break

    def odpocznij(self):
        if self.zycie == self.maks_zycie:
            print("Jesteś w pełni wypoczęty.")
        else:
            self.zycie += 1
            print(f"{self.nazwa} odpoczął.")

        print(f"Twoje życie wynosi: {self.zycie}/{self.maks_zycie}")


class Przeciwnik(Postac):
    def __init__(self):
        potwor = choice(['goblin', 'szkielet', 'zombie'])
        super().__init__(
            potwor,
            randint(0, 10),
            10
        )


imie_gracza = input('Podaj imię gracza: ')
gracz = Gracz(imie_gracza)

while True:
    akcja = input("Co chcesz zrobić? (zwiedzaj, odpocznij): ")

    if akcja == 'zwiedzaj':
        szansa = randint(0, 1)
        if szansa == 0:
            print(f"{gracz.nazwa} znalazł jaskinię.")
        elif szansa == 1:
            przeciwnik = Przeciwnik()
            gracz.walcz(przeciwnik)
    elif akcja == 'odpocznij':
        gracz.odpocznij()
    else:
        print("Nieznana akcja!")
