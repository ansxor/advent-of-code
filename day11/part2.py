file = open('input.txt', 'r')
input = [list(x.strip()) for x in file.readlines()]

dirs = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]

def cycle(xin):
    lx, ly = len(xin[0]), len(xin)
    out = [z.copy() for z in xin]
    def transform(x, y):
        if out[y][x] != '.':
            count = 0
            for t in dirs:
                tx, ty = t
                dist = 1
                while 0 <= tx*dist+x < lx and 0 <= ty*dist+y < ly:
                    if xin[y+ty*dist][x+tx*dist] == '#':
                        count += 1
                        if count >= 5:
                            out[y][x] = 'L'
                            return
                        break
                    if xin[y+ty*dist][x+tx*dist] == 'L':
                        break
                    dist += 1
            if count == 0:
                out[y][x] = '#'
    for y in range(len(xin)):
        for x in range(len(xin[y])):
            transform(x, y)
    return out

def gen_hash(l):
    return "".join(["".join(x) for x in l])

old = gen_hash(input)
l = cycle(input)
while old != (n := gen_hash(l)):
    old = n
    l = cycle(l)

print()
print(gen_hash(l).count('#'))
