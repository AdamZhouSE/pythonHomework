T=int(input())

for i in range(0,T):
    temp1=list(input().split(" "))
    x=int(temp1[1])
    temp=list(input().split(" "))
    lists=[]
    for i in range(0,len(temp)):
        lists.append(int(temp[i]))

    res=0
    for num in lists:
        if num%x==0:
            res=res|num

    print(res)


