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
        self.data = self._originaldata
        self.pos = 0

    def __init__(self, data):
        self._originaldata = data
        self.data = data
        self.pos = 0

file = open('input.txt')
data = [int(x) for x in file.read().split(',')]

data[1] = 12
data[2] = 2

computer = IntcodeComputer(data)

computer.run()
print(computer.data[0])