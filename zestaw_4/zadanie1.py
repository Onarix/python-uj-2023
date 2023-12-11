"""Zadanie ma na celu sprawdzenie jak wygląda tworzenie obiektów dla typów z wielokrotnym dziedziczeniem, jakie funkcje __new__ oraz __init__ są lub nie są wywoływane. 
Wychodzimy od dwóch klas bazowych (identycznych, różnią się tylko nazwą), class Baza(object) oraz class A(object) – patrz plik zadanie1.py. 
Posiadają one napisane __new__, __init__, __str__ oraz funkcję id(). 
Proszę przestudiować kilka różnych wariantów klas potomnych (B, C, D…) oraz tworzenia odpowiednich obiektów. 
Proponowane scenariusze są zapisane w pliku, klasy potomne powinny mieć zawartość zbliżoną, w celach studyjnych, do klas bazowych. 
W programie uruchomieniowym prezentować (oraz potrafić przedyskutować co się dzieje) różne scenariusze, włączając zagadnienie MRO (Method Resolution Order)."""


class Baza(object):
    def __new__(cls, *args):
        print("-> Baza __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- Baza __new__")
        return nowy_obiekt

    def __init__(self, x):
        print("-> Baza __init__", x)
        super().__init__()
        print("-- Baza __init__")
        self.x = x
        print("<- Baza __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-Baza-")


class A(object):
    def __new__(cls, *args):
        print("-> A __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- A __new__")
        return nowy_obiekt

    def __init__(self, x):
        print("-> A __init__", x)
        super().__init__(x)
        print("-- A __init__")
        self.x = x
        print("<- A __init__")

    def __str__(self):
        return "{self.x}".format(self=self)

    def id(self):
        print("-A-")


class B(Baza):
    def __new__(cls, *args):
        print("-> B __new__", *args)
        nowy_obiekt = Baza.__new__(cls)
        print("<- B __new__")
        return nowy_obiekt


class C(B):
    def __new__(cls, *args):
        print("-> C __new__", *args)
        nowy_obiekt = B.__new__(cls)
        print("<- C __new__")
        return nowy_obiekt


class D(A, C, B, Baza):
    # tu nie definiować __new__
    pass


### SCENARIUSZ 1:
print("SCENARIUSZ 1: \n")
print(B.mro())
b = B(123)
print("------------")
b.id()
print("------------")
print(b)
print("------------\n")

### SCENARIUSZ 2:
print("SCENARIUSZ 2: \n")
print(C.mro())
c = C(456)
print("------------")
c.id()
print("------------")
print(c)
print("------------\n")

### SCENARIUSZ 3:
print("SCENARIUSZ 3: \n")
print(D.mro())
d = D(789)
print("------------")
d.id()
print("------------")
print(d)
print("------------\n")

### SCENARIUSZ 4:
# tak jak 3, tylko zobaczyć, co się dzieje podczas rzutowania:
# A(d),id() albo B(d),id() itp.
print("SCENARIUSZ 4: \n")
print(D.mro())
d = D(789)
print("------------")
A(d).id()
print("------------")
print(d)
print("------------\n")
