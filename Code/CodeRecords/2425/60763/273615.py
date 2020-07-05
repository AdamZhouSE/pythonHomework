T = int(input())
for i in range(T):
    nk = list(map(int, ('' + input()).split(' ')))
    n,k = nk[0],nk[1]
    a = list(map(int, ('' + input()).split(' ')))
    a.sort()
    b = 0
    j = 0
    while j < n:
        if a[j] > k:
            break
        j += 1
    if j == 0:
        print(a[0])
    elif 2*k >= a[j] + a[j-1]:
        print(a[j])
    else:
        print(a[j-1])