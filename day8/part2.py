file = open('input.txt', 'r')
contents = file.read()
dimensions = (25, 6)
size = dimensions[0] * dimensions[1]
layers = []
image = [2 for x in range(25 * 6)]

for i in range(0, len(contents), size):
    layers.append([int(x) for x in contents[i:i+size]])

sum_of_zeros = [
    sum(y == 0 for y in x) for x in layers
]

largest_zero_list = layers[sum_of_zeros.index(min(sum_of_zeros))]
result = sum(x == 1 for x in largest_zero_list)
result *= sum(x == 2 for x in largest_zero_list)

for i in layers:
    for j in range(len(i)):
        if image[j] == 2 and i[j] != 2:
            image[j] = i[j]

output = ''
for i in range(dimensions[1]):
    for j in range(dimensions[0]):
        x = image[i*dimensions[0] + j]
        y = ' '
        if x == 1:
            y = '#'
        output += y
    output += '\n'

print(result)
print(output)