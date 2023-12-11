"""W pliku zadanie2.py (załączonym) znajduje się szkielet kodu klasy Zespolona. 
Posiada ona dwie składowe instancji, r (real) oraz i (imaginary), odpowiadające części rzeczywistej i urojonej liczby zespolonej. 
Dodatkowo zdefiniowane są funkcje sprzężenia zespolonego (conjugate) oraz fazy (argz). 
Reszta to szereg metod specjalnych __NNN__, których treść (w miejsce pass) należy napisać tak, żeby nastąpiło poprawne wykonanie kodu w funkcji main() – oczekiwane wyniki zapisano w komentarzu. 
Jeśli trzeba, to w Internecie poszukać informacje o liczbach zespolonych. 
Proszę zwrócić uwagę, że typ float czy int wymaga specjalnej obsługi w kodzie."""

from math import hypot, atan, sin, cos


class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        return (self.r * 2 + self.i * 2) ** 0.5

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.i})"

    def __str__(self):
        if self.i < 0:
            return f"({self.r}{self.i}j)"
        else:
            return f"({self.r}+{self.i}j)"

    def __add__(self, other):
        if isinstance(other, Zespolona):
            return Zespolona(self.r + other.r, self.i + other.i)
        else:
            return Zespolona(self.r + other, self.i)

    def __sub__(self, other):
        return Zespolona(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        if isinstance(other, Zespolona):
            return Zespolona(
                self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r
            )
        else:
            return Zespolona(self.r * other, self.i * other)

    def __radd__(self, other):
        return Zespolona(self.r + other, self.i)

    def __rmul__(self, other):
        return Zespolona(self.r * other, self.i * other)

    def __rsub__(self, other):
        return Zespolona(other - self.r, -self.i)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def __ne__(self, other):
        return not self.__eq__(other)

    def __pow__(self, n):
        result = Zespolona(1, 0)
        for i in range(n):
            result *= self
        return result


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a**2)
    print(b**4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)
