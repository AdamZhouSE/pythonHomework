list1=list(map(int,input().split(' ')))
n=list1[0]
k=list1[1]
ans=[]
for i in range(0,n+1):
    temp=[1,1]
    for j in range(1,k):
        temp.append(0)
    ans.append(temp)
for i in range(2,k+1):
    for j in range(1,n+1):
        temp=1
        while temp*j<=n:
            ans[temp*j][i]+=ans[j][i-1]
            temp+=1
res=0
for i in range(1,n+1):
    res+=ans[i][k]
    res%=1000000007
print(res)