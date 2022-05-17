import pygame
from Platforma import Platforma
from Kulka import Kulka

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

platforma = Platforma()

gra_dziala = True

while gra_dziala:
    # obsługa wyjścia z gry
    for zdarzenie in pygame.event.get():
        # naciśnięcie klawisza escape na klawiaturze
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False

            # elif zdarzenie.key == pygame.K_a:
            #     platforma.ruszaj_platforma(-1)
            # elif zdarzenie.key == pygame.K_d:
            #     platforma.ruszaj_platforma(1)

        # naciśnięcie krzyżyka na oknie aplikacji
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # obsługa sterowania platformą
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    elif keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)

    # renderowanie obiektów na ekranie
    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(platforma.surface, platforma.pozycja)

    # usuń wszystko co zostało wyrenderowane
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
