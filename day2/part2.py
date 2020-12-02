file = open("input.txt", 'r')
input = file.readlines()

result = 0

for i in input:
    z = i.split(':')
    letter = z[0].split(' ')[1]
    conditions = [int(x) for x in z[0].split(' ')[0].split('-')]
    count = z[1].count(letter)
    if (z[1][conditions[0]] == letter) != (z[1][conditions[1]] == letter):
        result += 1

print(result)