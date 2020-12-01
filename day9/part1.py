io_in, io_out = [], []

def intcode_input():
    if len(io_in) > 0:
        return io_in.pop()
    else:
        return input('Enter value: ')

def intcode_print(x):
    io_out.append(x)
    print(x)

class IntcodeComputer:
    def run(self):
        while self.complete == False:
            self.runcycle()
    
    def run_until_output(self):
        to_test = io_out.copy()
        while to_test == io_out and self.complete == False:
            self.runcycle()

    def runcycle(self):
        if self.data[self.pos] == 99:
            self.complete = True
            return
        opcode = self.data[self.pos]
        modes = [int(x) for x in '{:0>5}'.format(opcode)]
        opcode = modes.pop()
        modes = modes[0:3]
        modes.reverse()

        if opcode == 1:
            l, p = self.get_params(3, modes)
            self.data[l[2]] = p[0] + p[1]
            self.pos += 4
        elif opcode == 2:
            l, p = self.get_params(3, modes)
            self.data[l[2]] = p[0] * p[1]
            self.pos += 4
        elif opcode == 3:
            l, p = self.get_params(1, modes)
            self.data[l[0]] = intcode_input()
            self.pos += 2
        elif opcode == 4:
            l, p = self.get_params(1, modes)
            intcode_print(p[0])
            self.pos += 2
        elif opcode == 5:
            l, p = self.get_params(2, modes)
            if p[0] != 0:
                self.pos = p[1]
            else:
                self.pos += 3
        elif opcode == 6:
            l, p = self.get_params(2, modes)
            if p[0] == 0:
                self.pos = p[1]
            else:
                self.pos += 3
        elif opcode == 7:
            l, p = self.get_params(3, modes)
            if p[0] < p[1]:
                self.data[l[2]] = 1
            else:
                self.data[l[2]] = 0
            self.pos += 4
        elif opcode == 8:
            l, p = self.get_params(3, modes)
            if p[0] == p[1]:
                self.data[l[2]] = 1
            else:
                self.data[l[2]] = 0
            self.pos += 4
        elif opcode == 9:
            l, p = self.get_params(1, modes)
            self.rel += p[0]
            self.pos += 2
        else:
            raise ValueError
    
    def get_params(self, count, mode):
        """
        Parameter modes:
        - 0: position mode (gets parameters based on location in memory)
        - 1: immediate mode (gets parameters directly)
        - 2: relative mode (gets values relative to base)
        """
        locations = [int(x) for x in self.data[self.pos+1:self.pos+1+count]]
        params = []
        for x in range(len(locations)):
            # position mode 
            if mode[x] == 0:
                params.append(int(self.data[locations[x]]))
            # immediate mode
            elif mode[x] == 1:
                params.append(locations[x])
            # relative mode
            elif mode[x] == 2:
                params.append(int(self.data[locations[x]+self.rel]))
                print(self.rel)
        return locations, params 

    def reset(self):
        self.data = self._original_data.copy()
        self.complete = False
        self.pos = 0
        self.rel = 0

    def __init__(self, data):
        self._original_data = data.copy()
        self.data = data
        self.complete = False
        self.pos = 0
        self.rel = 0

file = open('input.txt', 'r')
contents = file.read()
data = [int(x) for x in contents.split(',')]
for i in range(2048):
    data.append(0)
computer = IntcodeComputer(data)
computer.run()