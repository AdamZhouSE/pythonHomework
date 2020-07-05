m = int(input())
for v in range(0, m):
    #n, x = map(int, input().split())
    num = int(input())
    i = 0
    k = 0
    while num > k:
        k = pow(2, i)
        i += 1
    print(k)