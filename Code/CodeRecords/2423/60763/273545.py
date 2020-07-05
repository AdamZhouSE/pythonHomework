T = int(input())
for i in range(T):
    mn = list(map(int, ('' + input()).split(' ')))
    m,n = mn[0],mn[1]
    M = list(map(int, ('' + input()).split(' ')))
    N = list(map(int, ('' + input()).split(' ')))
    a = set(M)
    b =set(N)
    if a.issubset(N):
        print("Yes")
    else:
        if b.issubset(M):
            print("Yes")
        else:
            print("No")