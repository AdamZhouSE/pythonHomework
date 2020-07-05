T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    lists=[]

    for x in temp:
        lists.append(int(x))

    res=-1
    for i in range(0,len(lists)):
        for j in range(i,len(lists)):
            if lists[j]>lists[i]:
                res=max(res,lists[j]-lists[i])

    print(res)