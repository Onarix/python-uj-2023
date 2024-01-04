#!/bin/python3
# https://www.hackerrank.com/challenges/matrix-script/problem

import math
import os
import random
import re
import sys

symbols = "#$%&"


def decode(matrix, cols):
    output = str()

    for i in range(cols):
        for row in matrix:
            output += str(row[i])

    return re.sub(r"(?<=[a-zA-Z])[#$%&\s]+(?=[a-zA-Z])", r" ", output)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(decode(matrix, m))
