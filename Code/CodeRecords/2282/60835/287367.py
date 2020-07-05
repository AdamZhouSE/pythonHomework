for o in range(int(input())):
    n = int(input())
    arrive = list(map(int,input().split()))
    leave = list(map(int,input().split()))
    res = 1
    for x in range(n):
        cnt = 1
        for y in range(x + 1, n):
            if arrive[y] < leave[x] and arrive[y] > arrive[x]:
                cnt = cnt + 1
        if cnt > res:
            res = cnt
    print(res)