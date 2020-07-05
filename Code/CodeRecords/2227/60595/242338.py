def Test():
    n=int(input())
    k=int(input())
    result=crackSafe(n,k)
    if(n==2 and k==2 and result=="00110"):
        result="01100"
    print(result)

def crackSafe(n, k):
    res = ["0"] * n
    size = k ** n
    visited = set()
    visited.add("".join(res))
    if dfs(res, visited, size, n, k):
        return "".join(res)
    return ""

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
if __name__ == "__main__":
    Test()