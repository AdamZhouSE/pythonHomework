# 5
n = int(input())
for i in range(n):
    N = int(input())
    l = []
    for i in range(2,N):
        if N%i == 0:
            l.append(i)
    print(l,N)
    if len(l) == 3:
        print(1)
    else:
        print(0)
        