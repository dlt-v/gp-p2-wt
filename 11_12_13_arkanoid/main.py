import pygame

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

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

    # renderowanie obiektów na ekranie
    ekran.blit(obraz_tla, (0, 0))
    # usuń wszystko co zostało wyrenderowane
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
