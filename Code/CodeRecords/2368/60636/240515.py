number=int(input())
lists=[]
for i in range(number):
    source=[]
    num=int(input())
    lis=input().split(" ")
    for i in range(num):
        source.append(int(lis[i]))
    lists.append(source)
for i in range(number):
    x=len(lists[i])
    res=[]
    for a in range(x):
        if(len(lists[i])!=0):
            res.append(lists[i][-1])
            lists[i].pop(-1)
        else:
            break
        if(len(lists[i])!=0):
            res.append(lists[i][0])
            lists[i].pop(0)
        else:
            break
    ans=""
    for y in res:
        ans=ans+str(y)+" "
    print(ans)