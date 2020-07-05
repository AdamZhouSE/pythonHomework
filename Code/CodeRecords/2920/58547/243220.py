n, k = map(int, input().split())
nl = list(map(int, input().split()))
b = []
for i in range(1, n):
    b.append(nl[i] - nl[i-1])
b.sort()
print(sum(b[:n-k]))