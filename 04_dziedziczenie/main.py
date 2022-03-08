"""
PRACA DOMOWA
Utwórz nową klasę, 2 metody, 2 atrybuty (właściwości) i nadaj mu konstruktor.
Jako klasę opisz zawód (np. informatyk, inżynier)
Utwórz z tej klasy 2 obiekty i zastosuj te metody.
"""


class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    # słowo kluczowe "self" odnosi się do tej klasy

    def pracuj(self):
        print(f'{self.imie} teraz pracuje.')

    def machaj(self):
        print(f'{self.imie} teraz macha rękoma.')


class Ksiegowy(Osoba):
    def __init__(self, imie, wiek, wydane_dokumenty, umiejetnosc_sortowania):
        super().__init__(imie, wiek)
        self.wydane_dokumenty = wydane_dokumenty
        self.umiejetnosc_sortowania = umiejetnosc_sortowania

    def sortuj(self):
        print(f'{self.imie} teraz sortuje.')


class Pracownik_zabki(Osoba):
    def __init__(self, imie, wiek, zmiana, umiejetnosc_kasowania):
        # ???
        super().__init__(imie, wiek)

        self.zmiana = zmiana
        self.umiejetnosc_kasowania = umiejetnosc_kasowania

    def obracaj_hotdogi(self):
        print(f'{self.imie} teraz obraca hotdogi.')


# tworzymy teraz obiekt/instancje klasy

pawel = Pracownik_zabki('paweł', 23, 'rano', 'mala')

# pawel.obracaj_hotdogi()
# pawel.machaj()

mateusz = Ksiegowy('mateusz', 60, 0, 'duze')
mateusz.pracuj()  # Osoba
mateusz.sortuj()  # Ksiegowy

"""
Zadanie Domowe
Utwórz klasę Zwierzę oraz jej podklasę (np. pies) i podaj w obu z nich po 2 atrybuty i 2 metody.
Przykład
Zwierze.jedz()

Pies.aportuj()

Tina = Pies(...)
Tina.jedz()
Tina.aportuj()
"""
