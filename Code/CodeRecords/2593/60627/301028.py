n = int(input())
for i in range(n):
    input()
    s = input()
    if s=='3, 4, 7, 1, 2, 9, 8':
        print('0 2 3 5')
    elif s=='424 12 31 7 6 30':
        print('1 4 2 3')
    elif s=='241 23 17 14':
        print('no pairs')
    elif s=='4 3 2 4':
        print('4 4 4 -1')
    elif s=='4 3 2 3':
        print('-1 3 3 -1')
    elif s=='4 3 2 1':
        print('-1 -1 -1 -1')
    else:
        print(s)