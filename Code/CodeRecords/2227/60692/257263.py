n = int(input())
k = int(input())
res = []
visited = set()
count = k ** n
ans = n * "0"
visited.add(ans)
for i in range(count):
    ans = ans[1:]
    for j in range(k):
        ans = ans + str(j)
        if ans not in visited:
            visited.add(ans)
            res.append(str(j))
            break
        ans = ans[0:n - 1]
res.reverse()
print("".join(res)+(n * "0"))