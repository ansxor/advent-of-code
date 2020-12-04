import numpy as np
from numpy.lib.function_base import append

file = open('input.txt', 'r')
input = file.read().split('\n\n')

keys = np.array([
    'ecl',
    'pid',
    'eyr',
    'hcl',
    'byr',
    'iyr',
    'hgt'
])

def create_passport(x):
    ret = {}

    inputs = x.strip().split()
    for i in inputs:
        j = i.split(':')
        k, v = j[0], j[1]
        ret[k] = v
    
    return ret

def is_valid_passport(x):
    ks = np.array(list(x.keys()))
    print(ks)
    return np.any(np.in1d(keys, ks))

elements = map(create_passport, input) 
valid = map(is_valid_passport, elements)

print(len(valid))