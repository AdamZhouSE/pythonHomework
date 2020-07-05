T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    lists=[]

    for x in temp:
        lists.append(int(x))

    res=0

    for i in range(0,len(lists)):
        for j in range(0,len(lists)):
            if lists[i]<lists[j]:
                res=max(res,j-i)

    print(res)