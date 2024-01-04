#!/bin/python3
#https://www.hackerrank.com/challenges/python-sort-sort/problem

import math
import os
import random
import re
import sys


def athSort(arr, k):
    return sorted(arr, key=lambda x: x[k])


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    for elem in athSort(arr, k):
        for item in elem:
            print(item, end=" ")
        print(end="\n")
