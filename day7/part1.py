import re

file = open('input.txt', 'r')
input = [x.strip() for x in file.readlines()]

bags = {}

def has_shiny_gold(dict, key):
    x = dict[key]
    if x.get('shiny gold') != None:
        return True
    if x.get('empty') == 1:
        return False
    for i in x:
        if has_shiny_gold(dict, i):
            return True
    return False

def bag_contents_count(dict, bag_name):
    x = dict[bag_name]
    amount = 0
    if x.get('empty') != 1:
        for i in x:
            to_add = bag_contents_count(dict, i)*x.get(i)
            to_add += x.get(i)
            amount += to_add
        return amount 
    return 0


for i in input:
    content = i.split(' contain ')
    in_bag = [x.strip() for x in content[1].split(',')]
    parent_bag = re.search('(\w+ \w+)', i).group(1)
    bags[parent_bag] = {}
    for j in in_bag:
        if re.search('(\w+ \w+) bag?', j).group(1) != 'no other':
            matches = re.search('(\d) (\w+ \w+) bag?', j)
            bags[parent_bag][matches.group(2)] = int(matches.group(1))
        else:
            bags[parent_bag]['empty'] = 1

shiny_bags = 0

for i in bags:
    if has_shiny_gold(bags, i):
        shiny_bags += 1

print(shiny_bags)
print(bag_contents_count(bags, 'shiny gold'))