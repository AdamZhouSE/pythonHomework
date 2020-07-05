def Test():
    mat=[]
    a=input()
    for i in range(4):
        s=input().strip()
        if(i!=3):
            s=s[:-1]
        mat.append(eval(s))
    b=input()
    print(deal(mat))

def deal(mat):
    row=len(mat)
    col=len(mat[0])
    dp=[]
    a=0
    for i in range(row+1):
        line=[]
        for j in range(col+1):
            line.append(0)
        dp.append(line)
    for i in range(row+1):
        for j in range(col+1):
            if(mat[i-1][j-1]=="0"):
                dp[i][j]=0
            else:
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                a=max(a,dp[i][j])
    return a*(a+1)

if __name__ == "__main__":
    Test()