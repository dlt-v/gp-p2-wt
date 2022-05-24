import pygame
import random

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

vec = pygame.math.Vector2


class Kulka(pygame.sprite.Sprite):

    def __init__(self):
        self.obraz = pygame.image.load("images/ball.png")
        self.zresetuj_pozycje()
        self.r = 16

    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU / 2, WYSOKOSC_EKRANU - 140)
        self.pozycja = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -30)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False

    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.pozycja.center = self.wspolrzedne  # type: ignore
        self.sprawdz_kolizje(platforma, klocki)

    def sprawdz_kolizje(self, platforma, klocki):

        # Sprawdź czy kulka dotyka krawędzi ekranu.
        if self.pozycja.x <= 0:
            self.wektor.x *= -1
        if self.pozycja.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1

        if self.pozycja.top <= 0:
            self.wektor.y *= -1
        if self.pozycja.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True

        # Sprawdź czy kulka dotyka krawędzi platformy.
        if self.pozycja.colliderect(platforma.pozycja):
            self.wektor.y *= -1
            if self.wektor.x < -10:
                self.wektor.x = -10
            if self.wektor.x > 10:
                self.wektor.x = 10

        for klocek in klocki:
            if self.kolizja_z_klockiem(self, klocek):
                klocek.uderzenie()
                break

    def kolizja_z_klockiem(self, kulka, klocek):
        dystans_x = abs(
            kulka.pozycja.centerx -
            klocek.pozycja.centerx
        ) - klocek.pozycja.w / 2

        dystans_y = abs(
            kulka.pozycja.centery -
            klocek.pozycja.centery
        ) - klocek.pozycja.h / 2

        if dystans_x < kulka.r and dystans_y < kulka.r:
            # odbicie po ścianie bocznej
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1

            return True
        else:
            return False
