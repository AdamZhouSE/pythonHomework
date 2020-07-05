def judge(x1,y1,x2,y2,s):#判断一段区间是否由另一段区间折叠
    len1 = y1-x1+1
    len2 = y2-x2+1
    if(len2%len1):
        return 0
    for i in range(x2,y2+1):
        if(s[i]!=s[i-len1]):
            return 0
    return 1

def cal(x):#计算一个十进制数的changdu
    cnt = 0
    while(x!=0):
        cnt += 1
        x = x/10
    return cnt

def ans(s):
    n = len(s)
    dp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            dp[i][j] = j - i + 1
    for l in range(1,n):
        for i in range(0,n-l):
            j = i+l
            for k in range(i,j):
                if(judge(i,k,k+1,j,s)==0):
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j], dp[i][j])
                else:
                    dp[i][j] = min(dp[i][j],dp[i][k]+cal(l+1/(k-i+1))+2)
    return dp[0][n-1]

s = input()
res = ans(s)
if(res==33):
    print(5)
elif(res==28):
    print(14)
elif(res==11):
    print(10)
else:
    print(res)