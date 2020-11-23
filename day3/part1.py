file = open('input.txt', 'r')
filelines = file.readlines()

wire = [x.split(',') for x in filelines]

# generate the wires
