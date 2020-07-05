import collections


# hamiliton graph 遍历所有点的方法

def numSquarefulPerms(A):
    N = len(A)
    count = collections.Counter(A)

    graph = {x: [] for x in count}
    for x in count:
        for y in count:
            if int((x + y) ** .5 + 0.5) ** 2 == x + y:
                graph[x].append(y)  # 添加与其匹配的数字

    def dfs(x, todo):  # 等待被访问的节点
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

    return sum(dfs(x, len(A) - 1) for x in count)


print(numSquarefulPerms([int(i) for i in input().split(",")]))
