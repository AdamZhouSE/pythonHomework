a=list(map(int,input().split(',')))
dp=[]
s=sum(a)
for i in range(len(a)//2+2):
    dp.append([])
for i in range(len(a)):
    for j in range(len(a)//2+1,0,-1):
        if j==1:
            dp[j].append(a[i])
        else:
            for k in range(len(dp[j-1])):
                dp[j].append(dp[j-1][k]+a[i])
sign=0
for i in range(1,len(dp)):
    tmp=s*i/len(a)
    for j in range(len(dp[i])):
        if tmp==dp[i][j]:
            sign=1
if sign==1:
    print('True')
else:
    print('False')