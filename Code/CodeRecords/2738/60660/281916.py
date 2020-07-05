ii='['
input()
temp=input()
while(temp!=']'):
    ii+=temp
    temp=input()
ii+=']'
l=eval(ii)
dp=[[0 for i in range(len(l[0]))] for j in range(len(l))]
result=0
for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j]=='0':
            continue
        dp[i][j]=dp[i][j-1]+1 if j else 1#计算该点的1最大宽度
        w=dp[i][j]
        for k in range(i,-1,-1):
            cw=dp[k][j]
            w=min(cw,w)
            area=w*(i-k+1)
            result=max(area,result)
print(result)