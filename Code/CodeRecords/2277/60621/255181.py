k=int(input())
n=int(input())
DP=[[-1 for j in range(n+1)] for i in range(k)]
#DP means the number of times when you have k eggs and need to check n floors
try:
    for i in range(n+1):
        DP[0][i]=i
    for j in range(1,k):
        DP[j][0]=0
        DP[j][1]=1
        DP[j][2]=2
    for i in range(1,k):
        x=1
        for j in range(3,n+1):
            while x<j and DP[i-1][x-1]<DP[i][j-x]:
                x+=1
            t1=max(DP[i-1][x-1],DP[i][j-x])
            if(x>=2):
                t2=max(DP[i-1][x-2],DP[i][j-x+1])
            else:
                t2=t1+1
            if(t1<t2):
                DP[i][j]=t1+1
            else:
                DP[i][j]=t2+1
                x-=1
    print(DP[k-1][n])
except BaseException:
    print(0)