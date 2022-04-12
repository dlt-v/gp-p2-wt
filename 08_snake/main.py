import pygame
import random
import time
from Jablko import Jablko

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

# Definicja ekranu i jego wymiarów oraz zegara gry.
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
        elif event.type == pygame.QUIT:
            game_running = False

    # Renderowanie elementów na ekranie.

    # Renderowawnie tła.
    ekran.blit(tlo, (0, 0))

    # Renderowanie jabłek.
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.pozycja)

    pygame.display.flip()
    zegar.tick(30)

time.sleep(3)
pygame.quit()
