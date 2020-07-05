T = int(input())
for _ in range(T):
    a = [int(x) for x in input().split(' ')]
    s = 0
    for i in range(a[1]):
        s += pow(2, i)
    print(s - a[0] + 1)
