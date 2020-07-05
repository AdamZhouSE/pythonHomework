T=int(input())
ans=[]
for i in range(T):
    temp=input().split(',')
    for j in range(int(temp[0]),int(temp[1])+1):
        ans.append([j,int(temp[2])])
ans.sort()
for i in range(len(ans)-1,0,-1):
    if ans[i][0]==ans[i-1][0]:
        ans[i-1][1]=ans[i-1][1]+ans[i][1]
        ans.pop(i)
ans.sort()
result=[]
for i in range(len(ans)):
    result.append(ans[i][1])
print(result)