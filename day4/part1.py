import re

file = open('input.txt', 'r')
input = [int(x) for x in file.read().split('-')]

count = 0

for i in range(input[0], input[1]):
    condition = True
    
    double_rx = re.compile(r'(.)\1')
    num = '{:0>6}'.format(i)
    nums = [int(x) for x in num]
    double = False
    not_decreasing = True
    oldnum = 0
    for j in nums:
        if j < oldnum:
            not_decreasing = False
            break
        if j == oldnum:
            double = True
        oldnum = j
    if not_decreasing and double:
        count += 1

print(count)
