def so(w):
    left, right = 0, len(w) - 1
    while left < right:
        if w[left] != w[right]:
            return False
        right -= 1
        left += 1
    return True
n= eval(input())
res, ans = [], 0
for i in range(0, n):
    res.append(input().split()[1])
for i in range(0, n):
    for j in range(0, n):
        if so(res[i] + res[j]):
            ans += 1
print(ans)