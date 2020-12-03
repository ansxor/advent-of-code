file = open('input.txt', 'r')


w, h = 3, 1
input = [y.strip() for y in file.readlines()]

x, y = 0, 0
tree = 0

while y < len(input):
    i = input[y]
    print(i, x, i[x % len(i)])
    if i[x % len(i)] == '#':
        tree += 1
    x += w
    y += h

print(tree)