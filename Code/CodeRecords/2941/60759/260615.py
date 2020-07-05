n = int(input())
grades = input()
pattern = ['F', 'D', 'C', 'B', 'A']
grade = 0
for ch in grades:
    if ch != 'E':
        grade += pattern.index(ch)
if grade == 0:
    print(0, end='')
else:
    print('{:.14f}'.format(grade / n), end='')
