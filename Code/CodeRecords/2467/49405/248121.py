T = int(input())
for t in range(T):
    m, n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b
    c.sort()
    print(c[k - 1])