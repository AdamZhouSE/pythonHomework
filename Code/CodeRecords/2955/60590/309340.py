a=input();len1=len(a)
b=input();len2=len(b)
k=int(input())
dp=[]
if len(a)==0:
    print(k*len(b))
    exit()
if len(b)==0:
    print(k*len(a))
    exit()
for i in range(len(a)+1):
    dp.append([])
    for j in range(len(b)+1):
        if i==0 or j ==0:
            dp[i].append(max(i,j)*k)
        else:
            dp[i].append(0)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        dp[i][j]=min(dp[i-1][j]+k,dp[i][j-1]+k,dp[i-1][j-1]+abs(ord(a[i-1])-ord(b[j-1])))
print(dp[len(a)][len(b)],end='')