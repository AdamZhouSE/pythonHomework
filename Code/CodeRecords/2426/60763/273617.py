T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, ('' + input()).split(' ')))
    a.sort()
    print(a[n-1]*a[n-2]*a[n-3])