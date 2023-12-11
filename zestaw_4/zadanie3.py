"""Zadanie przeglądowe, w ramach którego należy napisać proste ilustrujące fragmenty kodu. 
Należy kierować się wskazówkami z pliku zadanie3.py tak, żeby: 
a) wyjaśnić zasadę funkcji instancji klasy, funkcji składowej klasy z użyciem dekoratora @classmethod, funkcji statycznej klasy z użyciem dekoratora @staticmethod 
b) klasę abstrakcyjną, dziedziczącą z klasy ABC oraz metodę abstrakcyjną z użyciem dekoratora @abstractmethod, wraz z klasami potomnymi i odpowiednimi implementacjami 
c) przykład atrybutu klasy definiowanego z pomocą dekoratora @property oraz odpowiedniego @nazwa.setter"""

# podpunkt A)
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo,
# tak, żeby kod poniżej drukował treści jak w komentarzach


class A(object):
    def foo(self, x):
        print(f"wykonanie foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"static_foo({x})")


a = A()
a.foo(123)  # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a, 123)  # ditto
a.class_foo(123)  # class_foo(<class '__main__.A'>, 123)
A.class_foo(123)  # ditto
a.static_foo(123)  # wykonanie static_foo(123)
A.static_foo(123)  # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod


class BaseClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


class SubClass1(BaseClass):
    def abstract_method(self):
        print("Implementation in SubClass1")


class SubClass2(BaseClass):
    def abstract_method(self):
        print("Implementation in SubClass2")


# Test
obj1 = SubClass1()
obj1.abstract_method()  # Output: Implementation in SubClass1

obj2 = SubClass2()
obj2.abstract_method()  # Output: Implementation in SubClass2


# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu
class MyClass:
    def __init__(self):
        self._my_attribute = None

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value


# Test
obj = MyClass()
obj.my_attribute = 42
print(obj.my_attribute)  # Output: 42
