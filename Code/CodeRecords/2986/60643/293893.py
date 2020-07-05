def findShortestPath(s1,s2):
    dp=[ [0] * (len(s2)+1) for _ in range (len(s1)+1) ]
    #第一行初始化
    for i in range(1,len(s2)+1):
        dp[0][i]=dp[0][i-1]+1
    #第二行初始化
    for i in range(1,len(s1)+1):
        dp[i][0]=dp[i-1][0]+1
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
    res=dp[-1][-1]#最后一行最后一列的元素
    return res


if __name__=="__main__":
    s1=input()
    s2=input()
    ans=findShortestPath(s1,s2)
    print(ans)