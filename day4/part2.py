import re

count = 0

for i in range(264793, 803936):
    condition = True

    double_rx = re.compile(r'(.)\1')
    num = '{:0>6}'.format(i)
    nums = [int(x) for x in num]
    double_num = 0
    double = False
    not_decreasing = True
    oldnum = 0
    for j in nums:
        if j < oldnum:
            not_decreasing = False
            break
        if j == oldnum:
            double_num += 1
        elif double_num == 1:
            double_num = 0
            double = True
        else:
            double_num = 0
        oldnum = j
    if double_num == 1:
        double = True
    if not_decreasing and double:
        count += 1

print(count)
