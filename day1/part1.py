file = open('input.txt', 'r')
numbers = [int(x) for x in file.readlines()]

for i in numbers:
    for j in numbers:
        if i + j == 2020:
            print(i * j)