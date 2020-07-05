T = int(input())
for i in range(T):
    s = ('' + input()).split(' ')
    s = list(map(int, s))
    N,P = s[0],s[1]
    t = ('' + input()).split(' ')
    t = list(map(int, t))
    isEqual = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if t[i]*t[j] == P:
                isEqual = True
                break
    if isEqual:
        print("Yes")
    else:
        print("No")