#https://www.hackerrank.com/challenges/ginorts/problem

def ginortS(S):
    return "".join(
        sorted(
            sorted(
                sorted(
                    sorted("".join(sorted(S, key=lambda x: x.islower()))),
                    key=lambda y: y.isupper(),
                ),
                key=lambda z: int(z) % 2 != 0 if z.isdigit() else False,
            ),
            key=lambda u: int(u) % 2 == 0 if u.isdigit() else False,
        )
    )


S = input()

print(ginortS(S))
