T = int(input())
for ttt in range(T):
    inner = input().strip().split()
    N, x = int(inner[0]), int(inner[1])
    aSet = set()
    bSet = set()
    for i in range(N):
        [aSet.add(int(i)) for i in input().strip().split()]
    for i in range(N):
        [bSet.add(int(i)) for i in input().strip().split()]
    res = 0
    for i in aSet:
        if x - i in bSet:
            res += 1
    print(res)