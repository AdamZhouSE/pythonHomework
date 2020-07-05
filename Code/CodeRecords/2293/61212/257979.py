T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    K=int(input())
    lists=[]

    for x in temp:
        lists.append(int(x))

    lists=set(lists)

    if K==1:
        print((min(lists)))
    else:
        for i in range(0,K-1):
            lists.remove(min(lists))

        print(min(lists))