file = open('input.txt', 'r')
input_orig = [x.strip() for x in file.readlines()]
command_map = list(map(lambda x: x.split()[0], input_orig))
input_map = [False for x in input_orig]
def iterasd():
    for i in [i for i, x in enumerate(command_map) if x == 'nop']:
        for j in [i for i, x in enumerate(command_map) if x == 'jmp']:
            input = input_orig.copy()
            input_map = [False for x in input_orig]
            input[i], input[j] = 'jmp '+input[i].split()[1], 'nop '+input[j].split()[1]

            pos = 0
            accumulator = 0

            while True:
                if pos >= len(input):
                    return accumulator
                elif input_map[pos] == True:
                    break
                else:
                    input_map[pos] = True
                cur = input[pos].split()
                ins, param = cur[0], int(cur[1])
                if ins == 'nop':
                    pos += 1
                elif ins == 'acc':
                    accumulator += param
                    pos += 1
                elif ins == 'jmp':
                    pos += param
    return -1

print(iterasd())