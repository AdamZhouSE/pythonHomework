import collections


def dfs(x, todo):
    count[x] -= 1
    if todo == 0:
        ans = 1
    else:
        ans = 0
        for y in graph[x]:
            if count[y]:
                ans += dfs(y, todo - 1)
    count[x] += 1
    return ans


arr = input().split(",")
for i in range(len(arr)): arr[i] = int(arr[i])
N = len(arr)
count = collections.Counter(arr)

graph = {x: [] for x in count}
for x in count:
    for y in count:
        if int((x + y) ** .5 + 0.5) ** 2 == x + y:
            graph[x].append(y)
print(sum(dfs(x, len(arr) - 1) for x in count))