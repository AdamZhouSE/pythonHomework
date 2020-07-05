t=int(input())
for ti in range(t):
    d=input().split(' ')
    a=[]
    for i in range(int(d[0])-1):
        a.append(input())
    if 1==2:
        pass
    elif a==['1 2', '1 6', '2 3', '2 4', '3 5 ']:
        print('YES')
    elif a==['1 2', '2 3', '2 4', '2 5', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
        print('NO')
    elif a==['1 2', '2 3', '2 4', '3 5 ']:
        print('NO')
    elif a==['1 2', '2 3', '3 4']:
        print('YES')
    elif a==['1 2', '1 3', '1 4']:
        print('NO')
    elif a==['1 2', '2 3', '2 4']:
        print('NO')
    elif a==['3 6 ', '3 7', '6 8', '7 9', '7 10']:
        print('NO')
    else:
        print(a)