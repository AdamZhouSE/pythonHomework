N = int(input())
grade = input().upper()
list(grade).sort()
sum = 0.00
for i in grade:
    if i == 'A':
        sum += 4
    elif i == 'B':
        sum += 3
    elif i == 'C':
        sum += 2
    elif i == 'D':
        sum += 1
sum /= N
if sum == 0.0:
    print(0, end='')
else:
    print(format(sum, '.14f'), end='')