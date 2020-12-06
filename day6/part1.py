file = open('input.txt', 'r')
input = [x.strip() for x in file.read().split('\n\n')]

count = 0

for i in input:
    x = set(i)
    x.discard('\n')
    count += len(x)

print(count)