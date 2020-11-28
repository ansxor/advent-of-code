file = open('input.txt', 'r')
filelines = file.readlines()

wire = [x.split(',') for x in filelines]

# generate the wires

def generate_wireset(wires):
    wireset = []
    current = [0, 0]
    for i in wires:
        new = [0, 0] 
        direction = i[0]
        length = int(i[1:])
        if direction == 'R':
            new = {'position': [current[0]+length, current[1]], 'direction': 'H'}
        elif direction == 'L':
            new = {'position': [current[0]-length, current[1]], 'direction': 'H'}
        elif direction == 'D':
            new = {'position': [current[0], current[1]+length], 'direction': 'V'}
        elif direction == 'U':
            new = {'position': [current[0], current[1]-length], 'direction': 'V'}
        else:
            raise ValueError
        new['oldposition'] = current.copy()
        wireset.append(new)
        current = new['position'].copy()
    return wireset

wiresets = [generate_wireset(x) for x in wire]

intersections = []

for i in wiresets[0]:
    for j in wiresets[1]:
        if i['direction'] != j['direction']:
            iold, ipos, jold, jpos = [], [], [], [] 
            if i['direction'] == 'H':
                iold, ipos = i['oldposition'], i['position']
                jold, jpos = j['oldposition'], j['position']
            elif i['direction'] == 'V':
                jold, jpos = i['oldposition'], i['position']
                iold, ipos = j['oldposition'], j['position']
            else:
                raise ValueError

            x, y = jpos[0], ipos[1]

            intersects_horizontally = False
            if not iold[0] < ipos[0]:
                iold, ipos = ipos, iold
            intersects_horizontally = iold[0] <= jpos[0] and jpos[0] <= ipos[0]

            intersects_vertically = False
            if not jold[1] < ipos[1]:
                jold, jpos = jpos, jold
            intersects_vertically = jold[1] <= ipos[1] and ipos[1] <= jpos[1]

            if intersects_vertically and intersects_horizontally:
                intersections.append([jpos[0], ipos[1]]) 

intersections.pop(0)

mindist = abs(intersections[0][0]) + abs(intersections[0][1])
for i in intersections:
    mindist = min([
        mindist,
        abs(i[0]) + abs(i[1]),
    ])


print(mindist)