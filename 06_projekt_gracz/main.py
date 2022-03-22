import pygame


class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka):
        super(Obraz, self).__init__()
        self.obraz = pygame.image.load(sciezka)


class Element():
    def __init__(self, typ):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1, 4):
            sciezka = f"images/{typ}{i}.png"
            self.lista_obrazow.append(Obraz(sciezka))

    def wybierz_nastepny(self):
        self.wybrany += 1
        if self.wybrany > 2:
            self.wybrany = 0

    def podaj_wybrany_obraz(self):
        return self.lista_obrazow[self.wybrany].obraz


class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__('head')


SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

# importowanie zasobów z folderu
obraz_tla = pygame.image.load("images/background.png")
obraz_bazy_postaci = pygame.image.load("images/base.png")

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_dziala = True

while gra_dziala:

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(obraz_bazy_postaci, (270, 130))

    pygame.display.flip()

    zegar.tick(30)

pygame.quit()
