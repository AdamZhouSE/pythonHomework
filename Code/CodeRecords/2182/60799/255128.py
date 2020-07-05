T = int(input())
for ttt in range(T):
    tt = input().strip().split()
    n, k = int(tt[0]), int(tt[1])
    res = 0
    for i in range(2, n + 1):
        res = int((res + k) % i)
    print(res+1)
