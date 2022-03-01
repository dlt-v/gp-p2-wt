# class Wojsko():
#     # cechy
#     ilosc_zolnierzy = 0
#     karabin = ""
#     naleznosc = ""
#     liczba_czolgow = 0

#     def __init__(self, ilosc, bron, naleznosc, czolgi):  # init -> initialize -> inicjalizuj
#         self.ilosc_zolnierzy = ilosc
#         self.karabin = bron
#         self.naleznosc = naleznosc
#         self.liczba_czolgow = czolgi

#     def ile_zolnierzy(self):
#         print(f"Wojsko {self.naleznosc} ma {self.ilosc_zolnierzy} żołnierzy.")

#     def dostarcz_posilki(self, ilosc_posilkow):
#         # self.ilosc_zolnierzy = self.ilosc_zolnierzy + ilosc_posilkow
#         self.ilosc_zolnierzy += ilosc_posilkow


# mazowsze = Wojsko(1000, "Beryl", "mazowsze", 3)
# mazowsze.ile_zolnierzy()
# mazowsze.dostarcz_posilki(1000)
# mazowsze.ile_zolnierzy()

# slask = Wojsko(1300, "Kałach", "śląsk", 2)
# slask.ile_zolnierzy()
# slask.dostarcz_posilki(200)
# slask.ile_zolnierzy()

"""
ZADANIE

Dodaj do swojej klasy jeszcze jedną metodę i jeszcze jeden właściwość.(atrybut, cecha)
Po tym dodaj konstruktor, który ustawia nasze właściwości.
Utwórz dwie instancje tej klasy i użyj tych metod.
"""


class Fridge:
    # Właściwości

    def __init__(self, przedmioty={}, kolor: str = 'bialy', pojemnosc: int = 100, zasilanie: float = 2):
        self.kolor = kolor
        self.pojemnosc = pojemnosc
        self.zasilanie = zasilanie
        print(przedmioty)  # przedmioty = "zielony"
        self.przedmioty = przedmioty  # self.przedmioty = "zielony"
        self.ilosc_przedmiotow = len(przedmioty.keys())

    def pokaz_atrybuty(self):
        print(self.kolor, self.pojemnosc, self.zasilanie, self.ilosc_przedmiotow)

    def steal(self):
        # self.ilosc_hams = 0.5
        # self.ilosc_cheeses = 0
        # self.ilosc_carrots = 0
        # self.ilosc_cauliflowers = 1
        # self.ilosc_cucumbers = 0
        # self.weight = 100
        # print("Ooo nie!!! Ktoś mnie okradł i zostawił połowę szynki i kalafiora")
        # self.drawer = []
        # print("Coooo!? Nawet z szuflad :'(")
        # print("No nic:(... przynajmniej będzie na zupe:D")
        pass


przedmioty_typowej_rodziny = {
    "pomidory": 2,
    "szynka": 20,
    "mleko": 3
}

Bosh_model_2014 = Fridge({}, 'zielony', 50, 1.3)

Bosh_domyslny_model = Fridge(przedmioty_typowej_rodziny)

"""
PRACA DOMOWA
Utwórz nową klasę, 2 metody, 2 atrybuty (właściwości) i nadaj mu konstruktor.
Jako klasę opisz zawód (informatyk, inżynier)
Utwórz z tej klasy 2 obiekty i zastosuj te metody.
"""
