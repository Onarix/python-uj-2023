'''|....|....|....|....|....|....|....|....|....|....|....|....|
   0    1    2    3    4    5    6    7    8    9   10   11   12'''

length = int(input("Input length: "))
meter = "|"
numbers = "0"

for i in range(length):
    meter = meter + "....|"
    #TODO: Ogarnąć liczby przy miarce - tak żeby ostatnia cyfra wielocyfrowej liczby była przy |
    numbers = numbers + ' '*(5-len(str(i))) + str(i+1)

print(meter)
print(numbers)