class IntcodeComputer:
    def run(self):
        while self.data[self.pos] != 99:
            opcode = self.data[self.pos]
            modes = [int(x) for x in '{:0>5}'.format(opcode)]
            modes = modes[0:3]

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
                print(l, p)
                self.data[l[0]] = input('Enter value: ')
                self.pos += 2
            elif opcode == 4:
                l, p = self.get_params(1, modes)
                print(self.data[l[1]])
                self.pos += 2

        pass
    
    def get_params(self, count, mode):
        """
        Parameter modes:
        - 0: position mode (gets parameters based on location in memory)
        - 1: immediate mode (gets parameters directly)
        """
        locations = self.data[self.pos+1:self.pos+1+count]
        params = []
        for x in range(len(locations)):
            # position mode 
            if mode[x] == 0:
                params.append(int(self.data[locations[x]]))
            elif mode[x] == 1:
                params.append(int(locations[x]))
        return locations, params 

    def reset(self):
        self.data = self._originaldata
        self.pos = 0

    def __init__(self, data):
        self._originaldata = data
        self.data = data
        self.pos = 0

file = open('input.txt', 'r')
contents = file.read()
data = [int(x) for x in contents.split(',')]
computer = IntcodeComputer(data)

computer.run()