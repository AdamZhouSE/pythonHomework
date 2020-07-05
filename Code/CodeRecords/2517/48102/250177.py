def search(ls: list) -> int:
    return dfs(0, 0, ls)


def dfs(sum_now: int, layer: int, ls: list) -> int:
    if layer == 4:
        if sum_now == 0:
            return 1
        else:
            return 0
    count = 0
    for i in ls[layer]:
        count += dfs(sum_now+i, layer+1, ls)
    return count


res = []
for j in range(4):
    temp = input().split(',')
    temp = list(map(int, temp))
    res.append(temp)
print(search(res))