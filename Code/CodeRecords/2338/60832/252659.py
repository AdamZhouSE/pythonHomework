All = int(input())

for i in range(0, All):
    temp = input().split()
    n = int(temp[0])
    x = int(temp[1])

    ar = list(map(int, input().split()))

    isPair = False
    for p in range(0, n - 1):
        if isPair:
            break
        for q in range(p + 1, n):
            if ar[p] + ar[q] == x:
                print('Yes')
                isPair=True
                break
    if not isPair:
        print('No')