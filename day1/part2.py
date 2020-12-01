file = open('input.txt', 'r')
numbers = [int(x) for x in file.readlines()]

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(k * i * j)