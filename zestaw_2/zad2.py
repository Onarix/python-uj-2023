"""
2. Dla dowolnego podanego łańcucha znakowego wypisać: 
-ile jest w nim słów (poprzez słowo rozumiemy ciąg co najmniej jednego znaku innego niż znak przestankowy, dla uproszczenia przyjmijmy, że liczymy a-z, A-Z i 0-9 jako coś, co składa się na słowa), 
-ile liter, 
-ile cyfr, oraz wypisać statystykę częstości występowania poszczególnych liter oraz cyfr.
"""

Punct_marks = [".", "-", ",", ":", ";", "...", "?", "!", "(", ")", '"', "\t", " "]
Letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "W",
    "X",
    "Y",
    "Z",
]
Digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def inspectString(string):
    words = 0
    isWord = False

    Letters_stat = dict([(s, 0) for s in Letters])
    Digits_stat = dict([(d, 0) for d in Digits])

    i = 0

    for s in string:
        if (s in Punct_marks) or (i == len(string) - 1):
            if isWord:
                words += 1
                isWord = False
        elif s in Letters:
            Letters_stat[s] += 1
            isWord = True
        elif s in Digits:
            Digits_stat[s] += 1
            isWord = True
        i += 1

    print("Words: " + str(words))
    print("Letters: " + str(sum(Letters_stat.values())))
    print("Digits: " + str(sum(Digits_stat.values())))
    print("Letters stat: " + str(Letters_stat))
    print("Digits stat: " + str(Digits_stat))


string = input("Input any string: ")
inspectString(string)
