n, k = map(int, input().strip().split(" "))
m = list(map(int, input().strip().split(" ")))
ans = []
for i in range(k):
    a, b = map(int, input().strip().split(" "))
    ans.append(min(m[a - 1:b]))
print(" ".join(map(str, ans)), end=" ")
