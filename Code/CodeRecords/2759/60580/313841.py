size = int(input())
for i in range(size):
    tL = input().split()
    m = int(tL[0])
    n = int(tL[1])
    a = int(tL[2])
    b = int(tL[3])
    result = 0
    j = m
    while j <= n:
        if j % a == 0 or j % b == 0:
            result += 1
        j += 1
    print(result)