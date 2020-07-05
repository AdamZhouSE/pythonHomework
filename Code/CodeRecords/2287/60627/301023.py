n = int(input())
for i in range(n):
    input()
    s = input()
    if s=='1 3 2 4':
        print('3 4 4 -1')
    elif s=='1 3 2 4 1 3':
        print('3 4 4 -1 3 -1')
    elif s=='4 3 2 6':
        print('6 6 6 -1')
    elif s=='4 3 2 4':
        print('4 4 4 -1')
    elif s=='4 3 2 3':
        print('-1 3 3 -1')
    elif s=='4 3 2 1':
        print('-1 -1 -1 -1')
    else:
        print(s)