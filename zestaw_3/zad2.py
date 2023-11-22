"""Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną"""


def recursive_reversal(L, left, right):
    if left >= right:
        return L
    else:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        return recursive_reversal(L, left + 1, right - 1)


def iterative_reversal(L, left, right):
    while left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
    return L


list1 = [1, 2, 3, 4]
print(list1)
print(recursive_reversal(list1, 0, 3))
print(iterative_reversal(list1, 0, 3))
