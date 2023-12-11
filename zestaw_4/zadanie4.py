"""Dynamiczny charakter języka Python nie pozwala na bezpośrednie przeładowywanie funkcji o tych samych nazwach, ale różnych argumentach. 
Z pomocą dekoratorów pojawiają się w język techniki emulujące takie zachowania. 
W ramach zadania proszę przestudiować materiał na temat singledispatch oraz singledispatchmethod z modułu functools oraz napisać dowolny kod ilustrujący te przypadki 
(inny niż w podanej dokumentacji)  https://docs.python.org/3/library/functools.html#functools.singledispatch"""

from functools import singledispatch, singledispatchmethod


# singledispatch
@singledispatch
def convert_to_meters(value, unit):
    print(f"Conversion not supported for {type(value)}")


@convert_to_meters.register(int)
@convert_to_meters.register(float)
def _(value, unit):
    if unit == "cm":
        print(f"{value} {unit} is equal to {value / 100} meters")
    elif unit == "mm":
        print(f"{value} {unit} is equal to {value / 1000} meters")
    else:
        print(f"Unsupported unit: {unit}")


@convert_to_meters.register(str)
def _(value, unit):
    print(f"String conversion not supported")


# Test
convert_to_meters(150, "cm")  # Output: 150 cm is equal to 1.5 meters
convert_to_meters(500, "mm")  # Output: 500 mm is equal to 0.5 meters
convert_to_meters(3.5, "m")  # Output: Unsupported unit: m
convert_to_meters("abc", "cm")  # Output: String conversion not supported


# singledispatchmethod
class Hero:
    name = str()
    level = str()

    @singledispatchmethod
    def __init__(self, arg):
        self.name = "nameless"
        self.level = 0

    @__init__.register
    def _(self, arg: str):
        self.name = arg
        self.level = 0

    @__init__.register
    def _(self, arg: int):
        self.name = "nameless"
        self.level = arg

    def __str__(self) -> str:
        return f"Name: {self.name}, level: {self.level}"


# Test
hero1 = Hero(None)  # Output: Name: nameless, level: 0
hero2 = Hero("John")  # Output: Name: John, level: 0
hero3 = Hero(15)  # Output: Name: nameless, level: 15

print(hero1)
print(hero2)
print(hero3)
