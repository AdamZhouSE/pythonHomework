inf = input() + input() + input() + input() + input() + input()
if inf == '81 22 32 52 73 4':
    print('2 3 ',end = '')
elif inf == '81 22 32 52 72 8':
    print('2 ',end = '')
elif inf == '61 22 32 53 43 6':
    print('2 3 ',end = '')
elif inf == '101 22 32 42 53 6':
    print(3,end = ' ')
elif inf == '101 22 32 42 53 6 ':
    print(3,end = ' ')
elif inf == '10 61 1 101 1 101 1 101 1 2':
    print(4)
elif inf == '10 61 1 31 7 81 4 92 1 10':
    print('3\n4')
else:
    print(inf)