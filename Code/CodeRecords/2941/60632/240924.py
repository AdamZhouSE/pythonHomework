n = int(input())
grades = list(input())
total = 0
for i in grades:
    if i == 'A':
        total += 4
    elif i == 'B':
        total += 3
    elif i == 'C':
        total += 2
    elif i == 'D':
        total += 1
    elif i == 'F':
        total += 0
gpa = total / n
print('{0:.14f}'.format(gpa))