"""Python jest językiem, w którym przy użyciu kodu o niewielkiej długości, ale z umiejętnym użyciem bibliotek, da się osiągnąć interesujące wyniki.
Wymaga to jednak zapoznania się z możliwościami różnych bibliotek, celem tego zadania jest właśnie podstawowe użycie biblioteki do rysowania: 
(matplotlib) oraz biblioteki numpy. 
Zadanie: napisać prosty i zwięzły program, który pozwoli na wczytanie wielomianu funkcji f(x) jako danej wejściowej (łańcuch znakowy) 
oraz przedział x (od – x_min, do – x_max). Cel: narysować ten wielomian za pomocą plt.plot(x_val, y_val), 
gdzie x_val i y_val to będą, odpowiednio, tablica wygenerowana za pomocą x_val = np.linspace(x_min, x_max, 200), 
a tablica y_val wyliczona z użyciem funkcji eval dla wartości z tablicy x_val."""

import matplotlib.pyplot as plt
import numpy as np
import re

poly_regex = re.compile(
    r"""([+-]?(?:(?:\d+x\^\d+)|(?:\d+x)|(?:\d+)|(?:x)))""", re.VERBOSE
)


def draw_polynomial(poly, x_min, x_max):
    if type(x_min) != int or type(x_max) != int:
        raise Exception("Value for x_min (or x_max) is not a number!")
    if not re.match(poly_regex, poly):
        raise Exception("The provided polynomial is invalid!")
    f = lambda x: eval(poly)
    x_val = np.linspace(x_min, x_max, 200)
    y_val = [f(x) for x in x_val]
    plt.plot(x_val, y_val)
    plt.title("Wykres wielomianu")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()


func = input("Input any polynomial: ")
x_min = int(input("Input x_min: "))
x_max = int(input("Input x_max: "))
draw_polynomial(func, x_min, x_max)
