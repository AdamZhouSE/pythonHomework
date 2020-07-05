t,k = map(int,input().split())
ans=[]
for j in range(t):
    tmp=list(map(int,input().split()))
    ans.append(tmp)
ans=[(k-abs(ans[i][0]-ans[j][0]))*(k-abs(ans[i][1]-ans[j][1])) if abs(ans[i][0]-ans[j][0])<k and abs(ans[i][1]-ans[j][1])<k else 0 for i in range(len(ans)) for j in range(i+1,len(ans))]
ans=list(filter(lambda x:x,ans))
if len(ans)==1:
    print(ans[0])
elif not ans:
    print(0)
else:
    print(-1)