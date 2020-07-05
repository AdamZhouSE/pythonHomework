m = int(input())
for v in range(0, m):
    #a, b = map(int, input().split())
    num = int(input())
    f = [0]*(num+1)
    f[1] = 1
    cnt = 1
    for i in range(2, num+1):
        tmp = 1
        for j in range(0, i):
            cnt += 1
            tmp *= cnt
        f[i] = f[i-1] + tmp
    print(f[num])