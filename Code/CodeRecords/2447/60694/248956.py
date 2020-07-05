m, n = map(int, input().split())
l = list(map(int, input().split()))
l.insert(0, -1)
ans = []
for i in range(n):
    start, end = map(int, input().split())
    ans.append(min(l[start:end+1]))
print(*ans, end='')
print(" ", end='')
