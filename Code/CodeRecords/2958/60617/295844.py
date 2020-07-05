global m
m=[0 for i in range(0,101)]
for i in range(1,10):
    m[i]=1
for i in range(10,100):
    m[i]=2
m[100]=3

def fold():
    global m
    str=input()
    dp=[[float("inf") for i in range(0,len(str)+1)] for i in range(0,len(str)+1)]
    for i in range(0,len(str)+1):
        dp[i][i]=1
    for l in range(2,len(str)+1):
        for i in range(1,len(str)):
            j=i+l-1
            while j<=len(str):
                for k in range(i,j):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
                for k in range(i,j):
                    length=k-i+1
                    if l%length!=0:
                        continue
                    else:
                        if isFold(i,j,length,str):
                            dp[i][j]=min(dp[i][j],dp[i][k]+2+m[l/length])
                j+=1
    if dp[1][len(str)]==4:
        print(str)
    print(dp[1][len(str)])
def isFold(l,r,len,str):
    for i in range(l-1,r):
        if str[i]!=str[(i-l)%len+l]:
            return False
    return True

if __name__=='__main__':
    fold()