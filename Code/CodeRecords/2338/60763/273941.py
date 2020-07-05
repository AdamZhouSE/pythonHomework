T = int(input())
for i in range(T):
    nx = list(map(int, ('' + input()).split(' ')))
    n,x = nx[0],nx[1]
    a = list(map(int, ('' + input()).split(' ')))
    isContain = False
    for j in range(n):
        for k in range(n):
            if j ==k:
                continue
            if a[j] + a[k] == x:
                isContain = True
                break
    if isContain:
        print("Yes")
    else:
        print("No")