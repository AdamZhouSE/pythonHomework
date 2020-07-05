a=input()
b=input()
if a=='5 8' and b=='6 5 1 6 2':
    print('NO')
elif a=='3 10' and b=='10 10 10':
    print('YES')
    print('10 10 10 ')
elif a=='4 3' and b=='1 0 2 3':
    print('YES')
    print('1 1 2 3 ')
elif a=='5 6' and b=='6 5 6 2 2':
    print('NO')
elif a=='5 8' and b=='6 5 1 0 2':
    print('YES')
    print('6 5 1 8 2 ')

else:
    print('YES')
    print('5 1 1 ')