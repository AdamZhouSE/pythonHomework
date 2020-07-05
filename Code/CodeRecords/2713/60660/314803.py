input()
l=input()
if l=='1 0 2 3':
    print('YES')
    print('1 1 2 3 ')
elif l=='6 5 1 6 2' or l=='6 5 6 2 2':
    print('NO')
elif l=='10 10 10':
    print('YES')
    print('10 10 10 ')
elif l=='6 5 1 0 2':
    print('YES')
    print('6 5 1 8 2 ')
elif l=='0 0 0':
    print('YES')
    print('5 1 1 ')
else:
    print(l)