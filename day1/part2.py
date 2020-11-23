file = open('input.txt', 'r')
file_lines = file.readlines()

input = [int(x) for x in file_lines]
result = 0

for i in input:
    toadd = i
    def calc(x):
        return x // 3 - 2
    while not calc(toadd) < 0:
        toadd = calc(toadd)
        result += toadd

print(result)