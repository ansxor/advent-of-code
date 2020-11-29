file = open('input.txt', 'r')
input = file.read().split('\n')
tree = {}

for i in input:
    pair = i.split(')')
    tree[pair[1]] = pair[0]

orbit_count = 0
keys = tree.keys()
for i in keys:
    x = tree[i]
    orbit_count += 1
    while x in keys:
        x = tree[x]
        orbit_count += 1

print(orbit_count)