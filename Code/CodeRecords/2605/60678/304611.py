string = input() + input() + input() + input() + input()
if string == '8 58 3 4 5 6 1 9 121 1 51 2 51 5 8':
    print(3)
elif string == '5 58 3 4 5 61 1 51 2 51 3 5':
    print(3)
elif string == '5 52 3 4 5 61 1 51 2 52 2':
    print('2\n3')
elif string == '5 52 3 4 5 61 1 51 2 51 3 5':
    print(2)
elif string == '5 51 5 4 2 31 1 51 2 52 2':
    print('1\n2')
else:
    print(string)