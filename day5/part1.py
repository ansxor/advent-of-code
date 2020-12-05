file = open('input.txt', 'r')
input = [x for x in file.readlines()]

rows, columns = 128, 8

# generate seat IDs
ids = []

for i in input:
    row_data, column_data = i[:7], i[-3:]
    row, column, crow, ccol = 0, 0, rows, columns
    for j in row_data:
        if j == 'B':
            row += crow / 2
        crow /= 2
        print(j, row)
    for j in column_data:
        if j == 'R':
            column += ccol / 2
        ccol /= 2
    ids.append(row * 8 + column) 

print(max(ids))