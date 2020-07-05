All = int(input())

for q in range(0, All):
    n = int(input())
    ar = list(map(int, input().split()))

    if n % 2 == 0:
        print(0)
    else:
        ar.sort()
        for i in range(0, n, 2):
            if i == n - 1:
                print(ar[i])
                break
            if ar[i + 1] != ar[i]:
                print(ar[i])
                break
