m = int(input())
for v in range(0, m):
    #n, k = map(int, input().split())
    num = int(input())
    a = []
    a.append(num)
    t = 99999
    i = 0
    flag = True
    while t != num:
        if a[i] > 0 and flag:
            t = a[i] - 5
        else:
            flag = False
            t = a[i] + 5
        a.append(t)
        i += 1
    for i in a:
        print(i, end=' ')
    print('')