# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

f = lambda x: x**2


def maximize(lst, M):
    results = []
    for comb in list(product(*lst)):
        results.append(0)
        for elem in comb:
            results[-1] += f(elem)

    return max([res % M for res in results])


first_multiple_input = input().rstrip().split()

k = int(first_multiple_input[0])

m = int(first_multiple_input[1])

lists = list()

for _ in range(k):
    lists.append(list(map(int, input().rstrip().split())))

for elem in lists:
    elem.remove(elem[0])

print(maximize(lists, m))
