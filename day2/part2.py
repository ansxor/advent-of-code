import re

file = open("input.txt", 'r')
input = file.readlines()

result = 0

for i in input:
    m = re.search('(\\d+)-(\\d+) ([a-z]):( [a-z]+)', i)
    mn, mx, letter, string = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    count = string.count(letter)
    if (string[mn] == letter) != (string[mx] == letter):
        result += 1

print(result)