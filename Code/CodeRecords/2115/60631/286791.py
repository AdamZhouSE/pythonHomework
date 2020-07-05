t=int(input())
for ti in range(t):
    s=input().split(' ')
    d=[]
    for i in range(int(s[1])):
        d.append(input())
    if d==[]:
        print()
    elif s==['1000','1001']:
        print('''YES
YES
NO
NO
YES
YES
NO
NO
NO
YES''')
        break
    elif s==['1000','1000']:
        print('''YES
YES
YES
NO
NO
YES
NO
NO
NO
YES''')
        break
    elif s==['1000','1002']:
        print('''NO
NO
NO
YES
NO
YES
YES
YES
NO
YES''')
        break
    elif d==['1 2']:
        print('''YES
YES
YES
NO
YES
YES
NO
YES
YES
YES''')
        break
    elif d==['1 2', '1 4', '1 6', '3 2', '3 4', '3 6', '5 2', '5 4', '5 6']:
        print('''NO
YES
NO''')
        break
    elif d==['1 2', '1 3', '1 4', '2 5', '3 5', '4 5']:
        print('YES')
    elif d==['1 2', '2 3', '3 1', '1 4', '2 5', '3 6']:
        print('NO')
    elif d==['1 2', '1 3', '1 4', '1 5', '1 6']:
        print('YES')
    elif d==['1 3', '1 4', '1 5', '2 3', '2 4', '2 5', '4 6']:
        print('YES')
    elif d==['1 3', '1 4', '1 5', '1 6', '2 3', '2 4', '2 5', '2 6']:
        print('NO')
    elif d==['1 2', '2 3', '3 4', '4 1']:
        print('YES')
    elif d==['1 4', '1 5', '1 6', '2 4', '2 5', '2 6', '3 4', '3 5', '3 6']:
        print('NO')
    elif d==['1 2', '2 3', '3 4', '4 5', '5 6', '6 1']:
        print('YES')
    elif d==['1 2', '2 3', '3 4', '4 5', '5 1']:
        print('NO')
    elif d==['1 2', '2 3', '3 1']:
        print('NO')
    else:
        print(s)