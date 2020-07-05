total = int(input())
lst = []
ans = 0
for line in range(total):
    lst.append(list(map(int, input().split(','))))
for l in range(total):
    for r in range(len(lst[0])):
        if lst[l][r] != 0:
            ans += 2
        for nl, nr in ((l - 1, r), (l + 1, r), (l, r - 1), (l, r + 1)):
            if 0 <= nl < total and 0 <= nr < total:
                ans += max(lst[l][r] - lst[nl][nr], 0)
            else:
                ans += lst[l][r]
print(ans)
