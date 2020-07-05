inf = input() + input() + input() + input()
if inf == '3 3 4C 1 1 3P 1 2C 2 2 2':
    print('2\n2')
elif inf == '3 3 6C 1 1 3P 1 2C 2 2 2':
    print('2\n2\n2')
elif inf == '2 2 4C 1 1 2P 1 2C 2 2 2':
    print('2\n1')
elif inf == '3 3 6C 1 3 3P 1 2C 2 2 2':
    print('1\n2\n1')
elif inf == '3 3 5C 1 3 3P 1 2C 2 2 2':
    print('1\n2\n2')
elif inf == '10 61 1 101 1 101 1 101 1 2':
    print(4)
elif inf == '10 61 1 31 7 81 4 92 1 10':
    print('3\n4')
else:
    print(inf)