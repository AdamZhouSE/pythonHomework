t = int(input())
result = []
for i in range(t):
    a1, a2 = map(int, input().split())
    n = int(input())
    d = a2 - a1
    result.append(a1 + (n - 1) * d)
for i in result:
    print(i)
