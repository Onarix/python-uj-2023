"""Dyskutowane w zadaniu poprzednim rozwiązania mają pewne ograniczenia, jest to nowa funkcjonalność w języku Python, która nadal nie obejmuje bardziej skomplikowanych zastosowań (np. przypadków dziedziczenia). 
W tym zadaniu przyjrzymy się zewnętrznemu modułowi multipledispatch (prawdopodobnie trzeba go najpierw zainstalować: pip install multipledispatch):
 https://github.com/mrocklin/multipledispatch/
Przykład w pliku zadanie5.py to klasy Figura, Prostokat, Kwadrat i chodzi o to, aby definiując poniżej wersje funkcji pole, różniące się argumentami oraz liczbą argumentów, wywołania wersji funkcji pole było uzależnione właśnie od argumentów. 
Jeśli ta selekcja ma się odbywać na więcej niż jednym argumencie, można właśnie użyc multipledispatch oraz dekorator @dispatch. 
Należy dopisać brakujący kod, aby testowe przykłady działały. P.s. jeszcze inna opcja, to zewnętrzny moduł plum
 https://github.com/beartype/plum"""

from multipledispatch import dispatch


class Figura(object):
    def __init__(self):
        print("Figura init")


class Prostokat(Figura):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


class Kwadrat(Prostokat):
    def __init__(self, x):
        super().__init__(x, x)


@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0


@dispatch(Prostokat)
def pole(instance: Prostokat):
    print("Pole: Prostokat")
    return instance.x * instance.y


@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x, y):
    print("Pole: Prostokat z dodatkowymi argumentami")
    instance.x = x
    instance.y = y
    return instance.x * instance.y


@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    print("Pole: Kwadrat")
    return instance.x * instance.y


@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, side):
    print("Pole: Kwadrat z podanym argumentem boku")
    instance.x = side
    instance.y = side
    return instance.x * instance.y


# testy

a, b, c = Figura(), Prostokat(2, 4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i))  # polymorphism at runtime


polaPowierzchni([a, b, c])
