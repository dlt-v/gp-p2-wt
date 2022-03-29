import pygame
import Element

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

# importowanie zasobów z folderu
obraz_tla = pygame.image.load("images/background.png")
obraz_bazy_postaci = pygame.image.load("images/base.png")
# elementy stroju
nakrycie_glowy = Element.NakrycieGlowy()
ubranie_element = Element.UbranieElement()
oczy_element = Element.OczyElement()
bron_element = Element.BronElement()


pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_dziala = True

while gra_dziala:

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            elif zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_w:
                oczy_element.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_e:
                ubranie_element.wybierz_nastepny()
            elif zdarzenie.key == pygame.K_r:
                bron_element.wybierz_nastepny()


        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(obraz_bazy_postaci, (270, 130))

    # wyrenderuj ubranka i akcesoria
    ekran.blit(nakrycie_glowy.podaj_wybrany_obraz(), (270, 130))
    ekran.blit(ubranie_element.podaj_wybrany_obraz(), (270, 130))
    ekran.blit(oczy_element.podaj_wybrany_obraz(), (270, 130))
    ekran.blit(bron_element.podaj_wybrany_obraz(), (270, 130))

    pygame.display.flip()

    zegar.tick(30)

pygame.quit()
