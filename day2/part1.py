file = open("input.txt", 'r')
input = file.readlines()

result = 0

for i in input:
    z = i.split(':')
    letter = z[0].split(' ')[1]
    conditions = [int(x) for x in z[0].split(' ')[0].split('-')]
    count = z[1].count(letter)
    if conditions[0] <= count and conditions[1] >= count:
        result += 1

print(result)