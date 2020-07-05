n = int(input())
ans = [None]*200000
print(n + 1)
l = 1
r = n + 1
for i in range(n + 1, 0, -2):
    ans[i] = r
    ans[i - 1] = l
    l += 1
    r -= 1

for i in range(1, n + 2):
    print(ans[i], end=' ')