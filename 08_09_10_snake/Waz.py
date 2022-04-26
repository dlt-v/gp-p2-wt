import pygame
import copy
from Segment import Segment

from Kierunek import Kierunek


class Waz(pygame.sprite.Sprite):
    def __init__(self):

        # Załadowanie głowy węża.
        self.org_obraz = pygame.image.load("images/head.png")

        self.obraz = pygame.transform.rotate(self.org_obraz, 0)
        self.pozycja = self.obraz.get_rect(
            center=(400, 304))
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA
        # (x, y)
        self.ostatnia_pozycja = self.pozycja
        self.segmenty = []
        self.dodaj_segment = False

    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa = True

        if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False

        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(
            self.org_obraz, self.kierunek.value * - 90)

        self.ostatnia_pozycja = copy.deepcopy(self.pozycja)

        # poruszanie sie weza
        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostania_pozycja)

        # dodawanie kolejnego segmentu
            if self.dodaj_segment:
                nowy_segment = Segment()

                nowa_pozycja = None

                if(len(self.segmenty)) > 0:
                    nowa_pozycja = copy.deepcopy(self.segmenty[i-1].pozycja)
                else:
                    nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
                    nowy_segment.pozycja = nowa_pozycja

                self.segmenty.append(nowy_segment)
                self.dodaj_segment = False

        # match self.kierunek:
        #     case Kierunek.GORA:
        #         self.pozycja.move_ip(0, -32)
        #     case Kierunek.DOL:
        #         self.pozycja.move_ip(0, 32)
        #     case Kierunek.LEWO:
        #         self.pozycja.move_ip(-32, 0)
        #     case Kierunek.PRAWO:
        #         self.pozycja.move_ip(32, 0)
        if self.kierunek == Kierunek.GORA:
            self.pozycja.move_ip(0, -32)
        if self.kierunek == Kierunek.DOL:
            self.pozycja.move_ip(0, 32)
        if self.kierunek == Kierunek.LEWO:
            self.pozycja.move_ip(-32, 0)
        if self.kierunek == Kierunek.PRAWO:
            self.pozycja.move_ip(32, 0)

    def rysuj_segmenty(self, ekran):
        for segment in self.segmenty:
            ekran.blit(segment.obraz, segment.pozycja)

    def jedz_jablko(self):
        self.dodaj_segment = True
