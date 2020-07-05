t = int(input())
for i in range(t):
    nk = input().split(" ")
    n, k = int(nk[0]), int(nk[1])
    a = input().split(" ")
    a = list(map(int, a))
    maxsum = 0
    for j in range(0, n-k+1):
        sum = 0
        for p in range(k):
            sum += a[j+p]
            if sum > maxsum:
                maxsum = sum
    print(maxsum)