t = int(input())
for i in range(0, t):
    n = int(input())
    a = input().split(" ")
    for i in range(0, n):
        a[i] = int(a[i])
    i = 0
    re = 0

    while i < len(a)-1:
        j = i+1
        while j < len(a):
            if a[i] > a[j] and j != len(a)-1:
                re += a[i] - a[j]
            elif a[i] > a[j] and j == len(a)-1:
                re -= (a[i] - a[j]) * (len(a) - 2)
                i = j
            else:
                i = j
            j += 1
    print(re)