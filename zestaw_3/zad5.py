"""W ramach zapoznania się z klasami, proszę napisać klasę o nazwie Bug taką, żeby zawierała licznik wskazujący aktualną liczbę powołanych do życia obiektów, identyfikator (lokalną zmienną obiektu, do której przypiszemy aktualny powiększony licznik). 
Licznik powinien rosnąć wraz z wywołaniem __init__ oraz maleć z wywołaniem __del__ (uwaga: współdzielony licznik będziemy używać w zapisie Bug.licznik). 
Proszę też zdefiniować __str__ wypisującą licznik i bieżące id. Proszę też napisać jakiś opisowy komentarz w klasie (w formie docstring). Finalnie, niech dla kodu:
```
bugs = []
for i in range(100):
bugs.append(Bug())
print(bugs[-1])
```
wypisują się licznik, identyfikator, a przy niszczeniu obiektu w __del__ niech będzie też print informacji typu 'Koniec', licznik, identyfikator."""


class Bug:
    licznik = 0

    def __init__(self):
        type(self).licznik += 1
        self.id = self.licznik

    def __del__(self):
        print(f"Koniec, {self.licznik}, {self.id}")
        type(self).licznik -= 1

    def __str__(self):
        return f"licznik = {self.licznik}, id = {self.id}"


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
