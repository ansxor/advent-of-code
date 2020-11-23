file = open('input.txt', 'r')
file_lines = file.readlines()

input = [int(x) for x in file_lines]
result = 0

for i in input:
    result += (i // 3) - 2

print(result)