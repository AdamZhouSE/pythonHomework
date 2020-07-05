k = int(input())
print(k + 1)
ans = [0 for i in range(k + 2)]
l, r = 0, k + 2
for i in range(k + 1, 0, -1):
    if (k - i + 2) % 2 == 1:
        r -= 1
        ans[i] = r
    else:
        l += 1
        ans[i] = l
print(' '.join(map(str, ans[1:])), end=' ')