def search18():
    str=input()
    dp=([[0]*len(str)]*len(str))
    for i in range(1,len(str)):
        if str[i]==str[0]:
            dp[i][0]=1
        if(str[0]==str[i]):
            dp[0][i]=1
    for i in range(1,len(str)):
        for j in range(1,len(str)):
            if(i!=j and str[i]==str[j]):
                dp[i][j]=dp[i-1][j-1]+1
    max=0
    x,y=0,0
    for i in range(1,len(str)):
        for j in range(1,len(str)):
            if(dp[i][j]>max):
                max=dp[i][j]
                x,y=i,j

    print(str[y-max+1:y+1])
    return

search18()