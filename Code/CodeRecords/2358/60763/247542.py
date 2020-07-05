T = int(input())
for i in range(T):
    s =  list(map(int,(''+input()).split(' ')))
    N = s[0]
    K = s[1]
    t = list(map(int, ('' + input()).split(' ')))
    t.sort()
    for i in range(K):
        print(t[N -1 - i],end=' ')
    print()