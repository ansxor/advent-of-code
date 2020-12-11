file = open('test.txt', 'r')
input = [list(x.strip()) for x in file.readlines()]

len_y, len_x = len(input), len(input[0])

def perform_cycle(input):
    output = [x.copy() for x in input]
    def check_adj(x, y):
        output[y][x] = '#'
        count = 0
        print(input[y])
        for test_y in range(-1, 2):
            for test_x in range(-1, 2):
                if (test_x, test_y) != (0, 0):
                    if 0 <= test_x+x < len_x and 0 <= test_y+y < len_y and input[y+test_y][x+test_x] == '#':
                        count += 1
                        print(count)
                    if count >= 4:
                        output[y][x] = 'L'
                        return
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == 'L':
                check_adj(x, y)
    return output

print(perform_cycle(perform_cycle(input.copy()).copy()))
