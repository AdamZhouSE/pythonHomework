lst = list(map(int, input().split(',')))
lst.sort()
ans = 0
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        ans += (lst[j] - lst[i]) * (2 ** (len(lst[i+1:j])))
print(ans % (10 ** 9 + 7))
