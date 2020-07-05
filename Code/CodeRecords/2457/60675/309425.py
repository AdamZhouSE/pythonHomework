
N = int(input())
happy = [] 
for i in range(N):
    happy.append(int(input()))
mat = [[0 for _ in range(N)] for _ in range(N)] 
for i in range(N-1):
    L, K = [int(x) for x in input().split()]
    mat[K-1][L-1] = 1
input()
dp = [[0, happy[m]] for m in range(N)]  


def dfs(p):  
    ind = -1
    sub = []
    while True: 
        try:
            ind = mat[p-1].index(1, ind+1)
            sub.append(ind)
        except ValueError:
            break
    if len(sub) == 0:
        dp[p-1][0] = 0
        dp[p-1][1] = happy[p-1]
        return
    for j in sub:
        dfs(j+1)
        dp[p-1][0] += max(dp[j][0], dp[j][1])
    for j in sub:
        dp[p-1][1] += dp[j][0]


headmaster = 1
for i in range(N): 
    flag = True
    for j in range(N):
        if mat[j][i] == 1:  
            flag = False
            break
    if flag:
        headmaster = i+1
        break
dfs(headmaster)
print(max(dp[headmaster-1]), end='')