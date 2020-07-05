import math
R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
table =[]
for i in range(0,R):
    for j in range(0,C):
        distance = int(math.fabs(i-r0))+int(math.fabs(j-c0))
        table.append(distance)

small =999
print('[',end='')
for i in range(0,R*C):
    print('[',end='')
    a=table.index(min(table))
    print(int(a/C),end=', ')
    print(a%C,end='')
    table[a]=999
    if i ==R*C-1:
        print(']]',end='')
        print()
    else:
        print(']',end=', ')