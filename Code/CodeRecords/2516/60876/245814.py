num=int(input())
lists=[]
for i in range(0,num):
    temp=list(map(int,input().split(",")))
    lists.append(temp)
result=[]
for item in lists:
    t=-1
    for items in lists:
        if items[0]>=item[1]:
            t=lists.index(items)
    result.append(t)
print(result)