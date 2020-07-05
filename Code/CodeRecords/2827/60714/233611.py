input()
ans = sorted([int(x) for x in input().split()])
for i in range(0, len(ans) - 1):
    print(ans[i], end=" ")
print(ans[len(ans) - 1])
