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
        new['length'] = length
        wireset.append(new)
        current = new['position'].copy()
    return wireset

def generate_intersections(wiresets):
    intersections = []
    ilength = 0
    for i in wiresets[0]:
        jlength = 0
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
                x2, y2 = iold[0], jold[1]
    
                intersects_horizontally = False
                if not iold[0] < ipos[0]:
                    iold, ipos = ipos, iold
                intersects_horizontally = iold[0] <= jpos[0] and jpos[0] <= ipos[0]
    
                intersects_vertically = False
                if not jold[1] < ipos[1]:
                    jold, jpos = jpos, jold
                intersects_vertically = jold[1] <= ipos[1] and ipos[1] <= jpos[1]
    
                if intersects_vertically and intersects_horizontally:
                    length_x = ilength + abs(x - x2)
                    length_y = jlength + abs(y2 - y)
                    intersections.append([x, y, length_x + length_y]) 
            jlength += j['length']
        ilength += i['length']
    if (intersections[0][0] == 0 and intersections[0][0] == 0):
        intersections.pop(0)
    return intersections

file = open('input.txt', 'r')

cases = [
    file.readlines(),
    [
        'R8,U5,L5,D3',
        'U7,R6,D4,L4'
    ],
    [
        'R75,D30,R83,U83,L12,D49,R71,U7,L72',
        'U62,R66,U55,R34,D71,R55,D58,R83'
    ],
    [
        'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
        'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    ]
]

for filelines in cases:
    wire = [x.split(',') for x in filelines]
    wiresets = [generate_wireset(x) for x in wire]

    intersections = []
    intersections = generate_intersections(wiresets)

    mindist = abs(intersections[0][0]) + abs(intersections[0][1])
    for i in intersections:
        mindist = min([
            mindist,
            abs(i[0]) + abs(i[1]),
        ])

    lengths = [x[2] for x in intersections]

    print(min(lengths), mindist)