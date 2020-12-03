import math
file = open('input.txt', 'r')


w, h = 3, 1
dirs = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]
dir = 0
input = [y.strip() for y in file.readlines()]

x, y = 0, 0
tree = 0

dir_len = []

for d in dirs:
    dir = 0
    w, h = d[0], d[1]
    x, y = 0, 0
    while y < len(input):
        i = input[y]
        if i[x % len(i)] == '#':
            dir += 1
        x += w
        y += h
    dir_len.append(dir)
    print(dir_len)

print(math.prod(dir_len))