All = int(input())

for q in range(0, All):
    temp = input().split()
    n = int(temp[0])
    k = int(temp[1])
    ar = list(map(int, input().split()))

    gap = abs(k - ar[0])
    for x in ar:
        if x > k:
            if gap >= x - k:
                print(x)
            else:
                print(k - gap)
            break

        if k - x < gap:
            gap = k - x
