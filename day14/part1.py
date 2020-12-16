import re
from functools import reduce

file = open('test2.txt', 'r')
input = [x.split(' = ') for x in file.readlines()]

mask = ''
mem = {}

for cmd, param in input:
    if cmd == 'mask':
        mask = list(param)
    else:
        num = list(format(int(re.search('mem\\[(\\d+)\\]', cmd).group(1)), '#0' + str(len(mask)+1) + 'b')[2:])
        print(num)
