import math

file = open('test.txt', 'r')
input = [x.strip() for x in file.readlines()]

way_x, way_y = 10, -1
x, y = 0, 0
d = 0

for i in input:
    action, param = i[0], int(i[1:])
    if action == 'F':
        tx, ty = way_x, way_y
        if d == 1:
            tx, ty = -way_y, way_x
        elif d == 2:
            tx, ty = -way_x, -way_y
        elif d == 3:
            tx, ty = way_y, -way_x
        print(way_x, way_y, d, tx, ty)
        if tx >= 0:
            print('east')
        else:
            print('west')
        if ty >= 0:
            print('south')
        else:
            print('north')
        x += tx * param
        y += ty * param
    elif action == 'R':
        print(param)
        d += param // 90
        d %= 4
    elif action == 'L':
        d -= (param // 90)
        while d < 0:
            d += 4
        d %= 4
    elif action == 'N':
        way_y -= param
    elif action == 'S':
        way_y += param
    elif action == 'E':
        way_x += param
    elif action == 'W':
        way_x -= param

print(abs(x) + abs(y))
