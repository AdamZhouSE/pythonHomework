def Test():
    n=int(input())
    line=eval("["+input().strip().replace(" ",",")+"]")
    root=[]
    dp=[]
    for i in range(0,40):
        c=[]
        for j in range(0,40):
            c.append(0)
        root.append(c)
        dp.append(c)
    def out_tree(l,r):
        if (l > r):
            return
        print("%d", root[l][r],end=" ")
        out_tree(l, root[l][r] - 1)
        out_tree(root[l][r] + 1, r)
    for i in range(1,n+1):
        dp[i][i]=line[i-1]
        dp[i][i - 1] = 1
        dp[i + 1][i] = 1
        root[i][i] = i
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            for j in range(i,i+l):
                if (dp[j][j] + dp[i][j - 1] * dp[j + 1][i + l - 1] > dp[i][i + l - 1]):
                    dp[i][i + l - 1] = dp[j][j] + dp[i][j - 1] * dp[j + 1][i + l - 1]
                    root[i][i + l - 1] = j
    print("%lld", dp[1][n])
    out_tree(1, n)
    print()
if __name__ == "__main__":
    Test()