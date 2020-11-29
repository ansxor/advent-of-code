file = open('input.txt', 'r')
contents = file.read()
dimensions = (25, 6)
size = dimensions[0] * dimensions[1]
layers = []

for i in range(0, len(contents), size):
    layers.append([int(x) for x in contents[i:i+size]])

sum_of_zeros = [
    sum(y == 0 for y in x) for x in layers
]

largest_zero_list = layers[sum_of_zeros.index(min(sum_of_zeros))]
result = sum(x == 1 for x in largest_zero_list)
result *= sum(x == 2 for x in largest_zero_list)

print(result)