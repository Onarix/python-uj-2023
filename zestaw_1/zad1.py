import sys

argv = sys.argv

for i in range(1, len(argv)):
    coef = list()
    coefs = ""
    div = 2
    num = int(float(sys.argv[i]))
    while num != 1:
        if (num % div) == 0:
            num = num / div
            coef.append(div)
        else:
            div = div + 1

    while len(coef) != 0:
        for x in coef:
            k = len([i for i, n in enumerate(coef) if n == x])
            while coef.count(x):
                coef.remove(x)
            if not coefs:
                if k == 1:
                    coefs = str(x)
                else:
                    coefs = str(x) + "^" + str(k)
            else:
                if k == 1:
                    coefs = coefs + "*" + str(x)
                else:
                    coefs = coefs + "*" + str(x) + "^" + str(k)
    print(sys.argv[i] + " = " + coefs)
