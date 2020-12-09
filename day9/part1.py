file = open('input.txt', 'r')
input = [int(x.strip()) for x in file.readlines()]

preamble_count = 25
number = 0

def generate_sums(x):
    for i in range(len(x)):
        for j in range(len(x)):
            print(i, j)
            if i != j:
                sums.append(x[i] + x[j])

for i in range(preamble_count, len(input)):
    preamble = input[i-preamble_count:i]
    number = input[i]
    sums = []
    for j in range(len(preamble)):
        for k in range(len(preamble)):
            if j != k:
                sums.append(preamble[j] + preamble[k])
    if not number in sums:
        break

print(number)