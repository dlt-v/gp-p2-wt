"""
klasa to jest przedstawienie jakiegoś elementu z realnego świata w postaci kodu
klasa posiada właściwości - np. kolor oczu, konie mechaniczne w silniku
klasa posiada również metody - czyli funkcje, np. klasa uczeń ma metodę ucz()


Jako przykład damy: blok z mieszkaniami
"""


# class Blok:  # nazwa klasy jest pisana z dużej litery
#     # właściwości
#     ilosc_okien = 40
#     kolor_scian_zewnetrznych = 'zielony'
#     ilosc_mieszkan = 20
#     ilosc_mieszkancow = 57
#     w_uzyciu = True

#     def zburz(self):  # metoda - słowo kluczowe self pozwala na operowanie na własnych zmiennych
#         self.ilosc_okien = 0
#         self.ilosc_mieszkan = 0
#         self.ilosc_mieszkancow = 0
#         self.w_uzyciu = False
#         self.kolor_scian_zewnetrznych = 'porysowany'
#         print('Budynek został zburzony.')


# podlaska7 = Blok()  # budujemy nowy blok
# # podlaska7 jest tak zwaną INSTANCJĄ klasy

# print(podlaska7.kolor_scian_zewnetrznych)  # -> zielony
# podlaska7.zburz()
# print(podlaska7.kolor_scian_zewnetrznych)

"""
Zad: Utworzyć 1 klase z 1 właściwością i 1 metodą.
"""


class Plecak:
    # właściwości
    przedmioty = []
    kolor = 'zielony'
    # metody

    def wloz(self, nowy_przedmiot):
        self.przedmioty.append(nowy_przedmiot)
        print('Przedmiot został włożony.')

    def wyjmij(self):
        if len(self.przedmioty) == 0:
            print('Plecak jest pusty.')
        else:
            wyjety_przedmiot = self.przedmioty.pop()
            print(f'Wyjęty przedmiot to {wyjety_przedmiot}')

    def zajrzyj(self):
        print(self.przedmioty)


nowy_plecak = Plecak()
nowy_plecak.zajrzyj()
nowy_plecak.wloz('kanapka')
nowy_plecak.wloz('ksiazka')
nowy_plecak.zajrzyj()
nowy_plecak.wyjmij()

"""
PRACA DOMOWA
Utwórz klasę z jakiegoś obiektu, który znajduje się w waszym pokoju.
Minimalnie 1 właściowość i 1 metoda.
"""
