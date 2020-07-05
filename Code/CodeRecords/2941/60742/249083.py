n = int(input())
grade = input()
sum = 0
for i in range(n):
    if grade[i]=='A':
        sum += 4
    elif grade[i]=='B':
        sum += 3
    elif grade[i]=='C':
        sum += 2
    elif grade[i]=='D':
        sum += 1
    else:
        sum += 0
if sum/n==0:
    print('0',end='')
else:
    print('{:.14f}'.format(sum/n),end='')