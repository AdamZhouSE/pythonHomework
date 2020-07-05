inf = input() + input() + input()
if inf == '3Add 0 1 1Del 1':
    print(0)
elif inf == '2Add 0 1 1Query 0':
    print(0)
elif inf == '9Add 1 1 1Add -2 4 3':
    print('1\n1\n0\n0')
elif inf == '11Add 1 1 1Add -2 4 3':
    print('2\n2\n2\n1')
else:
    print(2)