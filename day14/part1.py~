import re
from functools import reduce

file = open('input.txt', 'r')
input = [x.split(' = ') for x in file.readlines()]

mask = ''
mem = {}
print()

for cmd, param in input:
    if cmd == 'mask':
        mask = list(param)
    else:
        num = list(format(int(param), '#0' + str(len(mask)+1) + 'b')[2:])
        for i in range(len(num)):
            if mask[i] != 'X':
                num[i] = mask[i]
        mem[re.search('mem\\[(\\d+)\\]', cmd).group(1)] = int(''.join(num), 2)

print(sum(mem.values()))
