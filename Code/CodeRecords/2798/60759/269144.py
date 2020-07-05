n = int(input())
lst = list(map(int, input().split(' ')))
ans = 0
for i in range(1, len(lst)):
    for j in range(i + 1, len(lst)):
        if sum(lst[:i]) == sum(lst[i:j]) == sum(lst[j:]):
            ans += 1
print(ans)
