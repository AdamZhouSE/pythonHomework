def func(n,lis,m):
    set1=set(lis)
    dict={}
    for item in set1:
        dict.update({item:lis.count(item)})
    list1=list(dict.values())
    list1.sort()##从小到大
    x=m
    while(x>=0):
        if x>=list1[0]:
            x=x-list1[0]
            list1.remove(list1[0])
        else:
            x=-1
    return len(list1)

n=int(input())
ans=[]
for i in range(0,n):
    a=int(input())
    lis=input().split(" ")
    b=int(input())
    ans.append(func(a,lis,b))

for i in range(0,n):
    print(ans[i])