t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    d = b - a
    n = int(input())
    print(a + (n - 1) * d)
