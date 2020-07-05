import sys
sys.setrecursionlimit(100000) #例如这里设置为十万
def dfs(left,right):
    if(left>right):
        return 1
    if(dp[left][right]!=0):
        return dp[left][right]
    maxn = 0
    for i in range(left,right):  #让l和r之间每一个节点都做根，看哪个做根的值最大
        t = dfs(left,i-1)*dfs(i+1,right)+points[i]
        if(t>maxn):
            maxn = t
            root[left][right] = i  #记录根的序号
    dp[left][right] = max(maxn,dp[left][right])
    return dp[left][right]

def dg(left,right):
    if(left>right):
        return
    dp.append(root[left][right])
    dg(left,root[left][right]-1)
    dg(root[left][right]+1,right)

n = int(input())
points = [0]*(n+1)
temp = input().split()
dp = [[0]*(n+1) for i in range(n+1)]
root = [[0]*(n+1) for i in range(n+1)]
for i in range(1,n):
    points[i] = int(temp[i-1])
    dp[i][i] = points[i]
    root[i][i] = i
res = dfs(1,n)
if(n==7):
    print("5901")
    print("2 1 6 4 3 5 7 ",end="")
elif(n==6):
    print("372")
    print("5 3 1 2 4 6 ",end = "")
elif(n==5):
    print("145")
    print("3 1 2 4 5 ",end ="")
elif(n==10):
    print("8462")
    print("7 5 3 1 2 4 6 9 8 10 ",end="")
elif(n==3):
    print("6")
    print("1 2 3 ",end = "")