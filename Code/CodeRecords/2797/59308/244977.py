n = int(input())
a = [int(x) for x in input().split(' ')]

if len(a) == 1:
    if a[0] == 0:
        print('UP')
    elif a[0] == 15:
        print('DOWN')
    else:
        print(-1)
else:
    if a[len(a)-2] < a[len(a)-1]:
        if a[len(a)-1] != 15:
            print('UP')
        else:
            print('DOWN')
    else:
        if a[len(a)-1] == 0:
            print('UP')
        else:
            print('DOWN')




