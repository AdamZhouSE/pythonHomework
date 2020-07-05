n=int(input())
for i in range(n):
    k=int(input())
    list1=list(map(int,input().split(' ')))
    sum1=sum(list1)
    dp=[]
    for j in range(k+1):
        temp=[]
        for m in range(sum1//2+1):
            temp.append(0)
        dp.append(temp)
    for j in range(1,k+1):
        for m in range(1,sum1//2+1):
            if m >=list1[j-1]:
                dp[j][m] = max(dp[j - 1][m], dp[j - 1][m - list1[j - 1]] + list1[j - 1])
            else:
                dp[j][m]=dp[j-1][m]
    print(sum1-2*dp[k][sum1//2])