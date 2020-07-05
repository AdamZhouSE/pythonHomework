temp=[int(x) for x in input().split(" ")]
n,m,d=temp[0],temp[1],temp[2]
res=[]
for _ in range(n):
    temp = [int(x) for x in input().split(" ")]
    for i in range(m):res.append(temp[i])
res.sort()
flag=True
ans=[]
for i in range(len(res)):
    if (res[i]-res[0])%d!=0:
        flag=False
        break
    else:
        ans.append((res[i]-res[0])//d)
if not flag:print(-1)
else:
    result=0
    for i in ans:
        result+=abs(i-ans[len(ans)//2])
    print(result)