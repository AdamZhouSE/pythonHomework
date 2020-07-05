T = int(input())
for i in range(T):
    N = int(input())
    s = list(map(int,list(input().split(' '))))
    s.sort()
    t = list(map(int, list(input().split(' '))))
    t.sort()
    issame = True
    for j in range(N):
        if s[j] != t[j]:
            issame = False
            break
    if issame:
        print(1)
    else:
        print(0)