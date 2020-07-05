n=int(input())
nums=list(map(int,input().split(' ')))
list1=list(map(int,input().split(' ')))
visited=[]
for i in range(0,n):
    visited.append(0)
for i in list1:
    visited[i-1]=1
    res=0
    tot=0
    for j in range(0,n):
        if visited[j]==1:
            res=max(res,tot)
            tot=0
        else:
            tot+=nums[j]
    res=max(res,tot)
    print(res)