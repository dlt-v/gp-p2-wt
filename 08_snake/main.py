import pygame
import random
import time
from Jablko import Jablko
from Waz import Waz
from Kierunek import Kierunek

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608  # !!!

tlo = pygame.Surface((800, 608))

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(
            0, 20), random.randrange(0, 20))

        obraz.fill(maska,  special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))

pygame.init()

# Generowanie pojedynczego jabłka oraz dodanie go do grupy.
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

# Generowanie węża.
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

# Definicja ekranu i jego wymiarów oraz zegara gry.
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

game_running = True
while game_running:

    # Pętla wydarzeń.
    for event in pygame.event.get():

        # Naciśnięcie klawisza na klawiaturze.
        if event.type == pygame.KEYDOWN:

            # Klawisz Escape
            if event.key == pygame.K_ESCAPE:
                game_running = False

            if event.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)

            if event.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)

            if event.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)

            if event.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)

        elif event.type == PORUSZ_WEZEM:
            waz.aktualizuj()
        # Naciśnięcie krzyżyka.
        elif event.type == pygame.QUIT:
            game_running = False

    # Renderowanie elementów na ekranie.

    # Renderowawnie tła.
    ekran.blit(tlo, (0, 0))

    # Renderowanie węża.
    ekran.blit(waz.obraz, waz.pozycja)

    # Renderowanie jabłek.
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.pozycja)

    pygame.display.flip()
    zegar.tick(30)

time.sleep(3)
pygame.quit()
