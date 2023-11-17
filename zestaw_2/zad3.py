"""
3. Napisać program konwertujący liczby zapisane w systemie rzymskim (wielkimi literami I, V, X, L, C, D, M) 
na liczby arabskie w zakresie liczb 1-3999, i odwrotnie. Proszę kontrolować poprawność danych wejściowy, również w formacie rzymskim. 
Proszę spróbować napisać najbardziej kompaktowy (krótki) kod.
"""
import re

romanian = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

pattern = re.compile(r"""   
                        ^M{0,3}
                        (CM|CD|D?C{0,3})?
                        (XC|XL|L?X{0,3})?
                        (IX|IV|V?I{0,3})?$
        """, re.VERBOSE)

def romanianToArabic(n):
    if(not re.match(pattern, n)):
        raise Exception("The provided number is not valid!")
    res = 0
    i = 0
    while i < len(n):
        if (i < len(n) - 1):
            if(romanian.get(n[i] + n[i+1]) != None):
                res += romanian[n[i] + n[i+1]]
                i+=1
            elif(romanian.get(n[i]) != None):
                res += romanian[n[i]]
        elif(romanian.get(n[i]) != None):
            res += romanian[n[i]]
        i+=1
    return res

def arabicToRomanian(n):
    if (n < 1 or n > 3999):
        raise Exception("Value has to be in range 1-3999!")
    res = ""
    for (suf, val) in romanian.items():
        while n >= val:
            n -= val
            res += suf
    return res

rom = int(input("Input arabic number (1-3999): "))
print("Value in romanian: " + arabicToRomanian(rom))

arab = input("Input romanian number (I-MMMCMXCIX): ")
print("Value in romanian: " + str(romanianToArabic(arab)))