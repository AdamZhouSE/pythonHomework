All = int(input())

for q in range(0, All):
    temp = input().split()

    n = int(temp[0])
    k = int(temp[1])

    ar = [i for i in range(1, n + 1)]

    i = 0
    for p in range(n - 1):
        i = (k - 1 + i) % n
        del ar[i]
        n -= 1
    print(ar[0])
