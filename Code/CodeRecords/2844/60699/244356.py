
list1=list(map(int,input().split(' ')))
list2=list(map(int,input().split(' ')))
k=list1[1]
res=0
for i in range(0,len(list2)):
    temp=k
    for t in range(i,len(list2)):
        if temp>=list2[t]:
            temp-=list2[t]
            if t==len(list2)-1:
                res = max(res, t - i + 1)
        else:
            res=max(res,t-i)
            break
print(res)