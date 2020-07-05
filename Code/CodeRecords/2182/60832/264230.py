All = int(input())

for q in range(0, All):
    temp = input().split()

    n = int(temp[0])
    k = int(temp[1])

    time = 0

    ar = [i for i in range(1, n + 1)]

    i = 0
    while time < n - 1:
        t = 0
        while t < k:
            i = i % n
            if ar[i] != 0:
                t += 1
            i += 1
        ar[i-1] = 0
        time += 1

    for x in ar:
        if x != 0:
            print(x)
            break
