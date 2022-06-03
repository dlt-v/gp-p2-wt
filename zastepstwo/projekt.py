from Klocek import Klocek
from Kulka import Kulka
from Platforma import Platforma
import pygame

from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek

# wysokość i szerokość ekranu
SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
Poziom = 0
Zycia = 3

# ustawieniaimport pygame


pygame.init()
pygame.font.init()

Poziom = 0
Zycia = 3

czcionka = pygame.font.SysFont('Comic Sans MS', 24)
# utworzenie obiektu ekranu, zegara i tła
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

# poziomy gry
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

# utworzenie obiektu platformy
platforma = Platforma()

# utworzenie obiektu kulki
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
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)

    dodaj_klocki()


# główna pętla gry
gra_dziala = True

while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # get_pressed() -> zwraca wszystkie naciśnięte klawisze
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)

    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()

    # aktualizacja kulki
    kulka.aktualizuj(platforma)

    # sprawdzenie, czy kulka dotknęła dolnej krawędzi
    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    # aktualizacja platformy
    platforma.update()

    # rysowanie tła
    ekran.blit(obraz_tla, (0, 0))

    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.pozycja)

    # rysowanie platformy
    ekran.blit(platforma.obraz, platforma.rect)

    # rysowanie kulki
    ekran.blit(kulka.obraz, kulka.pozycja)

    # wyswietlenie liczby zyc
    tekst = czcionka.render(f"Życia: {Zycia}", False, (255, 255, 255))
    ekran.blit(tekst, (16, 16))

    # aktualizacja ekranu
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()  # wyjście z aplikacji gry pygame
pygame.init()
pygame.font.init()
