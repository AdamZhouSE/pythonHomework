def mini(N):
    res = ""
    for i in range(N):
        res = "0"+res
    while N>9:
        res = "9"+res
        N-=9
    res = str(N)+res
    return res


T = int(input())
for i in range(T):
    N = int(input())
    print(mini(N))
