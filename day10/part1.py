file = open('input.txt', 'r')
input = [int(x.strip()) for x in file.readlines()]

input.append(max(input) + 3)
input.append(0)

input.sort()

adaptor = [[], [], []]
plugged = []
for i in input:
    for j in range(1, 4):
        if i+j in input and not i+j in plugged:
            plugged.append(i+j)
            adaptor[j-1].append(i+j)
            break
        elif i-j != 0 and i-j in input and not i-j in plugged:
            plugged.append(i-j)
            adaptor[j-1].append(i-j)
            break

print(len(adaptor[0]) * len(adaptor[2]))