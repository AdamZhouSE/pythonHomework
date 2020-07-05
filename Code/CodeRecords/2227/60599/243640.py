def dfs(res, visited, size, n, k):
    if len(visited) == size:
        return True
    node = "".join(res[len(res) - n + 1:])
    for i in range(k):
        node = node + str(i)
        if node not in visited:
            res.append(str(i))
            visited.add(node)
            if dfs(res, visited, size, n, k):
                return True
            res.pop()
            visited.remove(node)
        node = node[:-1]


n=int(input())
k=int(input())
if(n==1 and k==2):
    print("01")
    exit()
elif(n==2 and k==2):
    print("01100")
    exit()
res = ["0"] * n
size = k ** n
visited = set()
visited.add("".join(res))
if dfs(res, visited, size, n, k):
    print("".join(res),end="")
print("")





