file = open('input.txt', 'r')
input = [x for x in file.readlines()]

rows, columns = 128, 8

# generate seat IDs
ids = []

for i in input:
    i = i.strip()
    row_data, column_data = i[:7], i[-3:]
    row, column, crow, ccol = 0, 0, rows, columns
    for j in row_data:
        crow //= 2
        if j == 'B':
            row += crow
    for j in column_data:
        ccol //= 2
        if j == 'R':
            column += ccol
    ids.append(row * 8 + column) 

ids.sort()
print(ids)

for i in range(min(ids), max(ids) - 2):
    if not ((i + 1) in ids):
        print(i+1)
        break