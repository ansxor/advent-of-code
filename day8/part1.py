file = open('input.txt', 'r')
input = [x.strip().split() for x in file.readlines()]
input_map = [False for x in input]

pos = 0
accumulator = 0

while True:
    if input_map[pos] == True:
        break
    else:
        input_map[pos] = True
    ins, param = input[pos][0], int(input[pos][1])
    if ins == 'nop':
        pos += 1
    elif ins == 'acc':
        accumulator += param
        pos += 1
    elif ins == 'jmp':
        pos += param

print(accumulator)