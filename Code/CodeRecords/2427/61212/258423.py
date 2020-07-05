T=int(input())

for k in range(0,T):
    num=int(input())
    temp=list(input().split(" "))
    lists=[]

    for x in temp:
        lists.append(int(x))

    a=False
    for i in range(0,len(lists)):
        if lists.count(lists[i])>1:
            print(i+1)
            a=True
            break

    if not a:
        print(-1)


