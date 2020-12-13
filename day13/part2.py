from functools import reduce

file = open('input.txt', 'r')

eat = file.readline()
ids = [x.strip() for x in file.readline().split(',')]

# https://github.com/mcpower/adventofcode/blob/master/2020/13/a-p2.py
# Chinese Remainder theorem probably need to learn that or something lol
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

n, a = [], []
for i, bus in enumerate(ids):
   if bus =='x':
       continue
   bus = int(bus)
   n.append(bus)
   a.append((-i) % bus)

print(chinese_remainder(n, a))
