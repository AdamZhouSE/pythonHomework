n = int(input())
for i in range(0, n):
    a, b = [int(x) for x in input().split()]
    c = b - a
    m = int(input())
    print(a + (m - 1) * c)
