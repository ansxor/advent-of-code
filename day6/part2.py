file = open('input.txt', 'r')
input = [x.strip() for x in file.read().split('\n\n')]

count = 0

for i in input:
    questions = None
    x = i.split()
    for j in x:
        y = set(j)
        if questions == None:
            questions = y
        else:
            questions = questions.intersection(y)
    questions.discard('\n')
    count += len(questions)

print(count)