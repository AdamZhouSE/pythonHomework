T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, ('' + input()).split(' ')))
    a.sort()
    for j in range(n-1):
        print(a[j],end=' ')
        # a2.append()
    print(a[n-1])