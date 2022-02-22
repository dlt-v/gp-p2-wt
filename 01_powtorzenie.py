
# # zmienne (i stałe)
# '''
# int - liczba całkowita 3, 16, 0, -16
# float - liczba zmiennoprzecinkowa 3.4 0.45 0.
# str - tekst/napis "Ala ma kota" "b" ""
# bool - prawda/falsz
# '''
# # operacje na zmiennych
# '''
# +, -, /, *
# / - dzielenie    8 / 3 =            2 i reszta 2
# // - dzielenie całkowite            2
# % - modulo/reszta z dzielenia  8 % 3 =         2
# **              2**2   2**(-2)
# '''
# # camelCase = 5
# snake_case = 11  # nie używamy polskich znaków, nazywanie zmiennych opisowo


# # struktury danych
# # numerowana, różne typy danych, w innych językach "tablica"
# example_list = ['a', 'a']
# # print(example_list[1])
# example_dictionary = {
#     'hair_color': 'blue',
#     'eye_color': 'blue'
# }
# print(example_list)
# # print(example_dictionary['hair_color'])

# """
#     Wprowadź swój, bądź wymyślony wygląd do obiektu

# """
# example_set = set(example_list)
# print(example_set)

# """
# set - zestaw UNIKALNYCH elementów  {'Tomek', 'Tomek'} = {'Tomek'}
# list - lista elementów ['Tomek', 'Tomek'] = ['Tomek', 'Tomek']
# dictionary - zbiór nazw i ich wartości  { 'imie': 'Tomek', 'nazwisko': 'Kowalski'}
# tuple - {'Tomek', 154}
# """

"""
    instrukcje warunkowe

    if <wyrażenie>:
        kod1
    elif <wyreżenie>:
        kod2
    else:
        kod3

    if <wyrażenie>:
        kod1
    if <wyreżenie>:
        kod2
    else:
        kod3

    Zadanie: Sprawdź czy przysługuje nam zniżka.
    < 18 lat - 20 %
    > 60 lat - 40 %


"""
klasa_gimnazjum = 4

# if klasa_gimnazjum == 2:
#     print('drugie pietro')
# elif klasa_gimnazjum == 1:
#     print('pierwsze piętro')
# else:
#     print('parter')

# match klasa_gimnazjum:
#     case 2:
#         print('drugie pietro')
#     case 1:
#         print('pierwsze pietro')
#     case 0:
#         print('parter')
#     case _:
#         print('nieprawidlowe dane')

"""
Zadanie: Sprawdź czy przysługuje nam zniżka.
    < 18 lat - 20 %
    > 60 lat - 40 %
"""

"""
petle
    for - służą nam do iterowania na elementach (np. napisy, listy)
    while - powtarzają jakiś kod w zależności od warunku

"""
activity_list = ['Tomek', 'Romek', 'Atomek', 'Paweł']
# for student in activity_list:
#     print(f'Czy {student} jest obecny?')

i = 0
while i < len(activity_list):
    if activity_list[i][-1] == 'k':
        print('Imię kończy się na k.')
    else:
        print('Imię nie kończy się na k.')
    i += 1

"""
    Utwórz listę uczniów w grupie i przeiteruj między nimi drukując ich imiona.
    Zrób to za pomocą fora.
"""
