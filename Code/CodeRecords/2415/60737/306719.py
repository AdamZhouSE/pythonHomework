maxn=35
dp, pre = [[0 for i in range(maxn)] for i in range(maxn)], [[0 for i in range(maxn)] for i in range(maxn)]


def dfs(l, r):
    if l>r:
        return
    x = pre[l][r]
    print(x, end=" ")
    dfs(l,x-1)
    dfs(x+1,r)

    
if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split( )]
    a.insert(0, 0)
    
    for leng in range(1, n+1):
        for l in range(n+2-leng):
            r = l+leng-1
            if l==r:
                dp[l][r] = a[l]
                pre[l][r] = l
            else:
                for k in range(l, r):
                    left=1
                    right=1
                    if k!=l: 
                        left = dp[l][k-1]
                    if r!=k: 
                        right = dp[k+1][r]

                    if dp[l][r] < left*right+a[k]:
                        dp[l][r] = left*right+a[k];
                        pre[l][r] = k

    print(dp[1][n])
    dfs(1,n)
    