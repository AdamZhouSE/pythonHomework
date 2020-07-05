n=int(input())
ans=[]
for i in range(n):
    temp=input().split(' ')
    ans.append(((int)(temp[0]),(int)(temp[1])))
ans.sort()
start=ans[0][0]
end=ans[0][1]
res=[]

for i in range(1,len(ans)):
    temp=ans[i]
    if end<temp[0]:
        res.append((start,end))
        start=temp[0]
        end=temp[1]
    else:
        end=max(temp[1],end)
res.append((start,end))
for j in res:
    print(j[0],end=" ")
    print(j[1])