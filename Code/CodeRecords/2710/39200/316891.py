N, Q = list(map(int, input().split()))
child = [0 for x in range(N)]
for i in range(Q):
    c, s, y = input().split()
    if c == 'M':
        child[int(y) - 1] = int(s)
    if c == 'D':
        flag = 0
        for x in range(int(y) - 1, N):
            if child[x] != 0 and child[x] <= int(s):
                flag = x + 1
                break
        if flag:
            print(flag)
        else:
            print(-1)

