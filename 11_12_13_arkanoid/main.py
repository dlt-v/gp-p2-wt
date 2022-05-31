import pygame
from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
Poziom = 0
Zycia = 3


ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")
# Poziomy gry
poziom1 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
poziom2 = [
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
poziom3 = [
    [2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
    [2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
    [2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
    [3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
    [0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
    [0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
    [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]

# Tworzymy zmienną platforma, która przechowuje instancje klasy Platforma.
platforma = Platforma()

kulka = Kulka()

klocki = pygame.sprite.Group()


def dodaj_klocki():
    wczytany_poziom = poziom1
    if Poziom == 0:
        wczytany_poziom = poziom1
    elif Poziom == 1:
        wczytany_poziom = poziom2
    elif Poziom == 2:
        wczytany_poziom = poziom3

    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(
                    32 + i * 96,
                    32 + j * 48,
                    wczytany_poziom[j][i]
                )
                klocki.add(klocek)


dodaj_klocki()

gra_dziala = True

while gra_dziala:
    # obsługa wyjścia z gry
    for zdarzenie in pygame.event.get():
        # naciśnięcie klawisza escape na klawiaturze
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False

        # naciśnięcie krzyżyka na oknie aplikacji
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # obsługa sterowania platformą
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    elif keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)

    # sprawdzenie czy pozostały jakieś bloczki na mapie
    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            # wyjdź z gry
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()

    # aktualizacja pozycji
    kulka.aktualizuj(platforma, klocki)
    klocki.update()
    platforma.aktualizuj()

    # renderowanie obiektów na ekranie
    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(platforma.surface, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)

    for cegielka in klocki:
        ekran.blit(cegielka.obraz, cegielka.pozycja)

    # usuń wszystko co zostało wyrenderowane
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
