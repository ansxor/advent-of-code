import re

count = 0

for i in range(0, 1000000):
    condition = True
    
    double_rx = re.compile(r'(.)\1')
    num = '{:0>6}'.format(i)
    nums = [int(x) for x in num]
    # check for double
    condition = double_rx.match(num) != None
    oldnum = 0
    for j in nums:
        if j < oldnum:
            condition = False
            break
        oldnum = j
    if condition:
        count += 1

print(count)
