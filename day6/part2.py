file = open('input.txt', 'r')
input = file.read().split('\n')
tree = {}

for i in input:
    pair = i.split(')')
    tree[pair[1]] = pair[0]

def build_map(x, t):
    orbit_map = []
    x = t[x]
    keys = t.keys()
    orbit_map.append(x) 
    while x in keys:
        x = t[x]
        orbit_map.append(x)
    return orbit_map

you_map = build_map("YOU", tree)
san_map = build_map("SAN", tree)

found = None
for i in you_map:
    if i in san_map:
        found = i
        break

if found != None:
    position = you_map.index(found) + san_map.index(found)
    print(position)
else:
    print("Path not found")