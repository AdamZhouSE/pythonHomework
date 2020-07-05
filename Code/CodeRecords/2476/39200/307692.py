t = int(input())
for x in range(t):
    n = int(input())
    Li = [int(i) for i in input().split()]
    Li.sort()
    s = 0
    for i in range(n):
        s += Li[i] * (n - i)
    print(s)
