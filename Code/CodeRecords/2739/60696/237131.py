visited = [False for i in range(9)]
groups = []
group = []


def dfs(step, start):
    if step == k:
        groups.append([j for j in group])
        return
    for i in range(start, 10):
        if visited[i-1]:
            continue
        visited[i-1] = True
        group.append(i)
        dfs(step+1, i+1)
        group.pop(-1)
        visited[i - 1] = False
    return


arr = input()
k = int(arr[0])
n = int(arr[-1])
dfs(0, 1)
res = []
for each in groups:
    if sum(each) == n:
        res.append(each)
print(res)