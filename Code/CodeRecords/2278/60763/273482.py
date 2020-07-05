T = int(input())
for i in range(T):
    n = int(input())
    a = ('' + input()).split(' ')
    a = list(map(int, a))
    a2 = []
    for j in range(n-1):
        print(a[j]^a[j+1],end=' ')
        # a2.append()
    print(a[n-1])