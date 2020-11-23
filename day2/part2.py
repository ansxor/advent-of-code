class IntcodeComputer:
    def run(self):
        while self.data[self.pos] != 99:
            opcode = self.data[self.pos]
            params_locations = self.data[self.pos+1:self.pos+4]
            params = [self.data[x] for x in params_locations]

            if opcode == 1:
                self.data[params_locations[2]] = params[0] + params[1]
            elif opcode == 2:
                self.data[params_locations[2]] = params[0] * params[1]

            self.pos += 4
        pass

    def reset(self):
        self.data = self._originaldata.copy()
        self.pos = 0

    def __init__(self, data):
        self._originaldata = data.copy()
        self.data = data
        self.pos = 0

file = open('input.txt')
data = [int(x) for x in file.read().split(',')]

data[1] = 12
data[2] = 2

computer = IntcodeComputer(data)

def find_params(computer, to_find):
    for i in range(100):
        for j in range(100):
            computer.reset()
            computer.data[1] = i
            computer.data[2] = j
            computer.run()
            if computer.data[0] == to_find:
                return i, j
    return None, None

noun, verb = find_params(computer, 19690720)
print(100 * noun + verb)