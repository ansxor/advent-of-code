class IntcodeComputer:
    def run(self):
        while self.data[self.pos] != 99:
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
                self.data[l[0]] = input('Enter value: ')
                self.pos += 2
            elif opcode == 4:
                l, p = self.get_params(1, modes)
                print(p[0])
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

        pass
    
    def get_params(self, count, mode):
        """
        Parameter modes:
        - 0: position mode (gets parameters based on location in memory)
        - 1: immediate mode (gets parameters directly)
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
        return locations, params 

    def reset(self):
        self.data = self._original_data
        self.pos = 0

    def __init__(self, data):
        self._original_data = data
        self.data = data
        self.pos = 0


file = open('input.txt', 'r')
contents = file.read()
data = [int(x) for x in contents.split(',')]
computer = IntcodeComputer(data)

computer.run()
