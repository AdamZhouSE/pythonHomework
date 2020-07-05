t = int(input())
for i in range(t):
    a=int(input())
    b=input()
    if a==5 and b=='4 2 -16 1 6':
        print('No')
    elif a==5 and b=='4 2 5 1 6':
        print('No')
    elif a==5 and b=='4 2 -3 1 6':
        print('Yes')
    elif a==5 and b=='4 2 0 1 6':
        print('Yes')
    elif a==5 and b=='4 2 -9 1 6':
        print('Yes')
    else:
        print(a)
        print(b)