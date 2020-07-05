tests = int(input())

for i in range(tests):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for j in range(n-1):
        for k in range(j, n):
            if l[j] > l[k]:
                c += 1
    print(c)
    c = 0
