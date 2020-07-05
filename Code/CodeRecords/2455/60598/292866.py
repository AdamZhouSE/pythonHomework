class Node:
    def __init__(self, x):
        self.val = x
        self.son = []


num = int(input())
temp = input()
if temp[-1] == ' ':
    temp = temp[0:-1]
dp = list(map(int, temp.split(" ")))
Nodes = [Node(dp[i]) for i in range(len(dp))]
ans = 0
for i in range(num-1):
    temp = input().split(" ")
    Nodes[int(temp[0]) - 1].son.append(int(temp[1]) - 1)
    Nodes[int(temp[1]) - 1].son.append(int(temp[0]) - 1)


def dfs(u, v):
    for s in Nodes[u].son:
        if s != v:
            dfs(s, u)
            dp[u] += max(0, dp[s])


dfs(1, 0)
print(max(dp),end="")
