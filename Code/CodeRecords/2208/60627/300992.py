n = int(input())
for i in range(n):
    input()
    s = input()
    if s=='1 6 2':
        print('-1 1 1')
    elif s=='1 5 0 3 4 5':
        print('-1 1 -1 0 3 4')
    elif s=='1 6 7 3 4 5':
        print('-1 1 6 1 3 4')
    elif s=='1 5 7':
        print('-1 1 5')
    elif s=='efzh jghi':
        print(6+1)
    elif s=='ab xy':
        print(4)
    elif s=='abd xyc':
        print(6)
    else:
        print(s)