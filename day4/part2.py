import re

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
    if result:
        # birth year
        result = result and (1920 <= int(x['byr']) <= 2002)
        # issue year
        result = result and (2010 <= int(x['iyr']) <= 2020)
        # expiration year
        result = result and (2020 <= int(x['eyr']) <= 2030)
        # height
        units = x['hgt'][-2:]
        if re.fullmatch('(cm|in)', units) != None:
            hgt = int(x['hgt'][:-2])
            if units == 'cm':
                result = result and (150 <= hgt and hgt <= 193)
            elif units == 'in':
                result = result and (59 <= hgt and hgt <= 76)
        else:
            result = False
        # hair color
        hcl_rx = re.compile(r'#[0-9a-f]{6}')
        result = result and hcl_rx.fullmatch(x['hcl']) != None
        # eye color
        result = result and x['ecl'] in [
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
        ]
        # pid
        pid_rx = re.compile('\d{9}')
        result = result and pid_rx.fullmatch(x['pid'])
        return result
    return False

elements = list(map(create_passport, input))
valid = list(filter(is_valid_passport, elements))

print(len(elements),len(valid))