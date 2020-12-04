file = open('input.txt', 'r')
input = file.read().split('\n\n')

keys = [
    'ecl',
    'pid',
    'eyr',
    'hcl',
    'byr',
    'iyr',
    'hgt'
]

def create_passport(x):
    ret = {}

    inputs = x.strip().split()
    for i in inputs:
        j = i.split(':')
        k, v = j[0], j[1]
        ret[k] = v
    
    return ret

def is_valid_passport(x):
    ks = list(x.keys())
    result = all(key in ks for key in keys) 
    return result

elements = list(map(create_passport, input))
valid = list(filter(is_valid_passport, elements))

print(len(elements),len(valid))