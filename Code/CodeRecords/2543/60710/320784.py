T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    lists=[]
    result=[]

    for i in range(0,len(temp)):
        lists.append(int(temp[i]))

    for i in range(1,len(lists)+1):
        res=min(lists)
        for j in range(0,len(lists)-i+1):
            window=lists[j:j+i]
            tempres=min(window)
            res=max(res,tempres)
        result.append(str(res))

    print(" ".join(result))