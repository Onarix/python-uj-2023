"""1. Mamy zagnieżdżoną listę, która może zawierać różne heterogeniczne typy, na przykład inną listę, ale również krotkę, słownik. 
Dodaj element o kolejnej wartości w najbardziej zagnieżdżonej liście. Napisz program, który zrobi to uniwersalnie, dla dowolnego zagnieżdżenia, również jeśli pojawią się inne typy.
Dla [1 [2, 3] 4] chodzi o [1 [2, 3, 4] 4], dla [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7] powinno być [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5, 6, 7]. 
Jeżeli największe zagnieżdżenie na danym poziomie się powtórzy, należy dodać w obu zagnieżdżeniach, czyli dla [1, [3], [2]] należy uzyskać [1, [3, 4], [2, 3]]. 
Przykład bardziej złożony: 
list1 = [1, 2, [3, 4, [5, {'klucz': [5, 6], 'tekst': [1, 2]}], 5], 'hello', 3, [4, 5], (5, (6, (1, [7, 8])))]. 
Tutaj na takim samym, największym poziomie zagnieżdżenia, są listy będące wartościami w słowniku (listy [5, 6], [1, 2]) a także zagnieżdżona w krotkach (lista [7, 8]) 
i do to do nich powinien zostać dodany kolejny element. Zatem oczekiwane jest: [1, 2, [3, 4, [5, {'klucz': [5, 6, 7], 'tekst': [1, 2, 3]}], 5], 'hello', 3, [4, 5, 6], (5, [6, [7, 8, 9]])]."""


def isStructure(elem):
    return (
        isinstance(elem, list)
        or isinstance(elem, dict)
        or isinstance(elem, tuple)
        or isinstance(elem, set)
    )


def addNextElemToMostNested(_list):
    to_add = dict()
    for elem in _list:
        count = 0
        queue = list()
        while isStructure(elem):
            count += 1
            if sum(isStructure(i) for i in elem) == 0 and not isinstance(elem, dict):
                if len(to_add) == 0 or any(i == count for i in to_add.values()):
                    if not any(isinstance(x, int) for x in elem):
                        elem.append(1)
                    else:
                        elem.append(max(elem) + 1)
                    to_add[str(elem)] = count
                elif any(i < count for i in to_add.values()):
                    to_add.clear()
                    if not any(isinstance(x, int) for x in elem):
                        elem.append(1)
                    else:
                        elem.append(max(elem) + 1)
                    to_add[str(elem)] = count
            if isinstance(elem, dict):
                elem = [item for item in elem.values() if isStructure(item)]
            elif sum(isStructure(i) for i in elem) > 1 or len(queue) > 0:
                if len(queue) == 0:
                    queue = [item for item in elem if isStructure(item)]
                elem = next((item for item in queue if (isStructure(item))), 0)
                queue.remove(elem)
                count -= 1
            else:
                elem = next((item for item in elem if (isStructure(item))), 0)
    return _list


# TEST
list1 = [
    1,
    2,
    [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
    "hello",
    3,
    [4, 5],
    (5, (6, (1, [7, 8]))),
]
print("list1 = " + str(list1))
print("modified list1 = " + str(addNextElemToMostNested(list1)))

print("\n")

list2 = [1, [2, 3], 4]
print("list2 = " + str(list2))
print("modified list2 = " + str(addNextElemToMostNested(list2)))

print("\n")

list3 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
print("list3 = " + str(list3))
print("modified list3 = " + str(addNextElemToMostNested(list3)))

print("\n")

list4 = [1, [3], [2]]
print("list4 = " + str(list4))
print("modified list4 = " + str(addNextElemToMostNested(list4)))

print("\n")

list5 = [1, 2, 3, ["hi", "hello"], 4]
print("list5 = " + str(list5))
print("modified list5 = " + str(addNextElemToMostNested(list5)))
